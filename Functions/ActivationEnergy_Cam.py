import glob
import pandas as pd
import matplotlib.pyplot  as plt
from Model       import Model                        as mod
from functions   import E_act_fixedtemp_biasvoltageN  as E_act
from functions   import E_act_fixedtemp_gatevoltage  as E_act_G
from functions   import chargeN                       as Q
import numpy as np

Fixed = {
    # 'Energy' : 7.37e-01,
    # 'lambda' : 1.47e-01,
    'T0'     : 298,
    'T1'     : 300
    }
    
initpar = {
    'Energy' : 0.69,
    'lambda' : 1.04,
    'cap'    :  1e-2,
    'A'      : -.75,
    'QWidth' :  0.15,
    'T0'     :  298,
    'T1'     :  300
    }

bnds = {
    'Energy' : [0,1],
    'lambda' : [0,1.5],
    'cap'    : [0,2],
    'A'      : [-2,0],
    'QWidth' : [0,1],
    'T0'     : [0,400],
    'T1'     : [0,400]
        } 


# metaData = pd.DataFrame()
colors = ['green', 'orange', 'red']
for file in glob.glob('Data\\Fixed\\*.txt'):
    newEntry = {}
    split = file.split('\\')[-1].split('.')[0].split('_')
    newEntry['mol']     = split[0]
    newEntry['V range'] = split[1]
    newEntry['n']       = int(split[2])
    newEntry['FileName'] = file.split('\\')[-1].split('.')[0]
    
    if not 'C' in newEntry['mol']: continue
    if not newEntry['V range'] == 'N': continue
    if not newEntry['n'] == 3: continue
    
    data = pd.read_csv(file, sep = '\t')
    plt.figure('Ea vs Vg')
    plt.scatter(data['V'], data['Ea'])
    
    xG = np.linspace(-1.2,0.2,100)
    vecEactG = np.vectorize(E_act_G)
    thrGate = vecEactG(xG, initpar['Energy'], initpar['lambda'], initpar['T0'], initpar['T1'])
    plt.plot(xG,thrGate, color=colors[newEntry['n']-1])
    
    plt.figure('Ea vs Vb')
    # plt.scatter(data['V'], data['Ea'])
    
    xG = np.linspace(-2,2,100)
    vecEactG = np.vectorize(E_act)
    thrGate = vecEactG(xG, *initpar.values())
    plt.plot(xG,thrGate, color=colors[newEntry['n']-1])
    
    plt.figure('Q vs Vb')
    # plt.scatter(data['V'], data['Ea'])
    
    xG = np.linspace(-2,2,100)
    vecEactG = np.vectorize(Q)
    thrGate = vecEactG(xG, initpar['A'], initpar['QWidth'])
    plt.plot(xG,thrGate, color=colors[newEntry['n']-1])
    
    print(newEntry['FileName'])
    EaModel = mod(E_act)
    EaModel.setParams(initpar,Fixed=Fixed, bnds = bnds)
    EaModel.fit(data['V'],data['Ea'], save = '%s.txt'%newEntry['FileName'], algorithm = 'LS', mode = 'verbose')
    EaModel.print(data['V'],data['Ea'],save = '%s.txt'%newEntry['FileName'])
    params = EaModel.parameters
    newEntry['Err']= EaModel.standardError(data['V'],data['Ea'])
    data['thr'] = EaModel.returnThry(data['V'])
    
    
    #Plotting Eact vs Bias and saving figure
    plt.figure('Eact Vs Bias %s' %newEntry['mol'])
    plt.scatter(data['V'],data['Ea'], color=colors[newEntry['n']-1], label = 'n == %d'%newEntry['n'])
    plt.plot(data['V'],data['thr'], color=colors[newEntry['n']-1])
    
    #Plotting Eact vs Gate and saving figure
    plt.figure('Eact Vs Gate %s' %newEntry['mol'])
    plt.scatter(data['V'],data['Ea'], color=colors[newEntry['n']-1], label = 'n == %d'%newEntry['n'])
    xG = np.linspace(-1.2,0.2,100)
    vecEactG = np.vectorize(E_act_G)
    thrGate = vecEactG(xG,params['Energy'],params['lambda'],params['T0'],params['T1'])
    plt.plot(xG,thrGate, color=colors[newEntry['n']-1])
    
    #Plotting Q vs Bias and saving figure
    plt.figure('Charging Vs Bias %s' %newEntry['mol'])
    xQ = np.linspace(-1,0,100)
    vecQ = np.vectorize(Q)
    thrQ = vecQ(xQ,params['A'],params['QWidth'])
    plt.plot(xQ,thrQ, color=colors[newEntry['n']-1])
    
    # metaData = metaData.append(pd.DataFrame(newEntry,index=[0]))    
del file
del newEntry
del split   