import glob
import pandas as pd
import matplotlib.pyplot  as plt
from Model       import Model                        as mod
from functions   import E_act_fixedtemp_biasvoltageN  as E_act
from functions   import E_act_fixedtemp_gatevoltage  as E_act_G
from functions   import chargeN                       as Q
import numpy as np

eaRange = 0

Fixed = {
    'Offset' :  6.5,
    'Energy' :  0.48,
    'lambda' :  0.04,
    'cap'    :  -0.56,
    'A'      :  -0.4,
    'QWidth' :  0.681,
    'T0'     :  298,
    'T1'     :  300
    }
alg = 'LS'  
initpar = {
    'Offset' :  5.92e+00,
    'Energy' :  4.69e-01,
    'lambda' :  1.30e-01,
    'cap'    :  -8.00e-01,
    'A'      :  -2.00e-01,
    'QWidth' :  1,
    'T0'     :  298,
    'T1'     :  300
    }

bnds = {
    'Offset' : [4.44,8.66],
    'Energy' : [0.32,0.61],
    'lambda' : [0.05,0.13],
    'cap'    : [-1,-0.20],
    'A'      : [-0.6,-0.1],
    'QWidth' : [0.47,0.75],
    'T0'     : [0,400],
    'T1'     : [0,400]
        }

try:
    bnds['A'][0] = -Fixed['Energy']
    print(bnds['A'])
except:
    print()

def edited_Eact(V,offset,E,l,cap,A,W,T0,T1):
    return E_act(V,E,l,cap,A,W,T0,T1)+offset

metaData = pd.DataFrame()
colors = ['green', 'orange', 'red']
test = pd.DataFrame()
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
    if not newEntry['n'] == 1: continue
    
    tempFix = Fixed.copy()
    # if 'cap' in Fixed:
    #     tempFix['cap'] = Fixed['cap']*newEntry['n']
    
    tempData = data[data['V']<-.538]
    EaModel = mod(edited_Eact)
    EaModel.setParams(initpar,Fixed=tempFix, bnds = bnds)
    # EaModel.fit(tempData['V'],tempData['Ea'], save = '%s_%d.txt'%(newEntry['FileName'],eaRange*100), algorithm = alg, mode = 'verbose')
    EaModel.print(data['V'],data['Ea'],save = '%s_%d.txt'%(newEntry['FileName'],eaRange*100))
    data['Eathr'] = EaModel.returnThry(data['V'])
    
    newEntry['Err']= EaModel.standardError(data['V'],data['Ea'])
    
    test['V']   = data['V']
    test['exp'] = data['Ea']
    test['thr'] = data['Eathr']
    #Grab fitted params for fitting of 
    params = EaModel.parameters
    for par in params.keys():
        newEntry[par] = params[par]
   
    V = np.arange(-1,0,.01)
    
    EaVect = np.vectorize(edited_Eact)
    Ythr = EaVect(V, *params.values())
    #Plotting Ea vs Vb
    plt.figure('Ea vs Vb')
    plt.scatter(data['V'], data['Ea'], color=colors[newEntry['n']-1])
    plt.plot(V, Ythr, color=colors[newEntry['n']-1])
    
    
    
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