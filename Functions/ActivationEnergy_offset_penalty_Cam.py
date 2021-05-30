import glob
import pandas as pd
import matplotlib.pyplot  as plt
from Model       import Model                        as mod
from functions   import E_act_fixedtemp_biasvoltageN  as E_act
from functions   import E_act_fixedtemp_gatevoltage  as E_act_G
from functions   import chargeN                       as Q
import numpy as np

eaRange = -.54

Fixed = {
    'Energy' : .7,
    # 'lambda' : 3.03e-01,
    # 'cap'    : -0.049,
    # 'A'      : -6.77e-01,
    # 'QWidth' : .3,
    'T0'     : 298,
    'T1'     : 300
    }
    
initpar = {
    'Offset' :  5,
    'Energy' :  .75,
    'lambda' :  1.57e-01,
    'cap'    : -1.27e+00,
    'A'      :  -7e-01,
    'QWidth' : 9.45e-01,
    'T0'     :  298,
    'T1'     :  300
    }

bnds = {
    'Offset' : [0,20],
    'Energy' : [0,1.5],
    'lambda' : [0,1],
    'cap'    : [-2.5,0],
    'A'      : [-1.5,0],
    'QWidth' : [0,.25],
    'T0'     : [0,400],
    'T1'     : [0,400]
        } 

# for key in initpar.keys():
#     parval = initpar[key]
#     diff = abs(parval*.05)
#     bnds[key] = [parval-diff, parval+diff]

def edited_Eact(V,offset,E,l,cap,A,W,T0,T1):
    return E_act(V,E,l,cap,A,W,T0,T1)+offset

metaData = pd.DataFrame()
colors = ['green', 'orange', 'red']
for file in glob.glob('Data\\Fixed\\*.txt'):
    newEntry = {}
    split = file.split('\\')[-1].split('.')[0].split('_')
    newEntry['mol']     = split[0]
    newEntry['V range'] = split[1]
    newEntry['n']       = int(split[2])
    newEntry['FileName'] = file.split('\\')[-1].split('.')[0]    
    data = pd.read_csv(file, sep = '\t')
    
    if newEntry['V range'] == 'P': continue
    if not 'C' in newEntry['mol']: continue
    # if not newEntry['n'] > 1: continue
    
    tempFix = Fixed.copy()
    if 'cap' in Fixed:
        tempFix['cap'] = Fixed['cap']*newEntry['n']
    
    tempData = data[data['V']<-.538]
    
    def minimizeEact(V,offset,E,l,cap,A,W,T0,T1):
        e_Eact = np.vectorize(edited_Eact)
        tempData['thr'] = e_Eact(tempData['V'],offset,E,l,cap,A,W,T0,T1)
        err = np.sqrt(np.sum(np.subtract(tempData['thr'],tempData['Ea'])**2))
        penalty = Q(0,A,W)
        return err+penalty*10
    
    EaModel = mod(minimizeEact)
    EaModel.setParams(initpar,Fixed=tempFix, bnds = bnds)
    EaModel.fit(tempData['V'],tempData['Ea'], save = '%s_min_%d.txt'%(newEntry['FileName'],eaRange*100), algorithm = 'diff', mode = 'verbose')
    EaModel.print(data['V'],data['Ea'],save = '%s_min_%d.txt'%(newEntry['FileName'],eaRange*100))
    data['Eathr'] = EaModel.returnThry(data['V'])
    
    newEntry['Err']= EaModel.standardError(data['V'],data['Ea'])
    
    #Plotting Ea vs Vb
    plt.figure('Ea vs Vb')
    plt.scatter(data['V'], data['Ea'], color=colors[newEntry['n']-1])
    plt.plot(data['V'], data['Eathr'], color=colors[newEntry['n']-1])
    
    #Grab fitted params for fitting of 
    params = EaModel.parameters
    for par in params.keys():
        newEntry[par] = params[par]
    
    #Plotting Ea vs Vg
    plt.figure('Ea vs Vg')
    plt.scatter(data['V'], data['Ea'], color=colors[newEntry['n']-1])
    vecEactG = np.vectorize(E_act_G)
    data['EaVsVg'] = vecEactG(data['V'], params['Energy'], params['lambda'], params['T0'], params['T1'])
    plt.plot(data['V'],data['EaVsVg'], color=colors[newEntry['n']-1])
             
    #Plotting Q vs Vg
    plt.figure('Q vs Vb')
    vecEactG = np.vectorize(Q)
    V = np.arange(-1,1,.01)
    Qthr = vecEactG(V, params['A'], params['QWidth'])
    plt.plot(V, Qthr, color=colors[newEntry['n']-1])
    
    #Plotting Vg vs Vb
    plt.figure('Vg vs Vb')
    vecEactG = np.vectorize(Q)
    plt.plot(V, Qthr*params['cap'], color=colors[newEntry['n']-1])
    
    metaData = metaData.append(pd.DataFrame(newEntry,index=[0]))    
del file
del newEntry
del split
del colors
del data

for par in metaData.keys():
    if par in ['n', 'mol', 'T1', 'T0','Err', 'FileName', 'V range']: continue
    plt.figure(par)
    plt.scatter(metaData['n'], metaData[par])

print('Total Error: %.7f'%np.sqrt(np.sum(metaData['Err']**2)))