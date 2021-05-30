# -*- coding: utf-8 -*-
"""
Created on Mon May 17 13:08:14 2021

@author: nickl
"""
import glob
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
from functions   import E_act_fixedtemp_biasvoltageN  as E_act

fixed = {
    'Energy' : .3,
    # 'lambda' : 3.03e-01,
    # 'QWidth' : 9.00e-02,
    'T0'     : 298,
    'T1'     : 300
    }

metaData = pd.DataFrame()
for file in glob.glob('Results\\*'):
    data = pd.read_csv(file, sep = '\t')
    n = int(file[-5])
    
    cut1 = data.copy()
    for par in fixed.keys():
        parRange = abs(fixed[par]*.05)
        parMin = fixed[par] - parRange
        parMax = fixed[par] + parRange
        
        cut1 = cut1[cut1[par]>parMin]
        cut1 = cut1[cut1[par]<parMax]
        
        del parRange
        del parMin
        del parMax
    
    MinErr = min(cut1['error'])
    MaxErr = min(cut1['error']*1.01)
    
    cut2 = cut1.copy()
    cut2 = cut2[cut2['error']<=MaxErr]
    
    newEntry = dict(data[data['error'] == MinErr].reset_index().iloc[0])
    del MinErr
    del MaxErr
    del newEntry['index']
    del newEntry['error']
    del file
    del par
    
    pars = list(newEntry.keys())
    for par in pars:
        newEntry['%s_STD'%par] = np.std(cut2[par])
    
    newEntry['n'] = n
    metaData = metaData.append(pd.DataFrame(newEntry,index=[0]))

for par in pars:
    if par in fixed.keys(): continue
    temp = metaData[metaData['n'] > 1]
    avg_weighted = np.average(temp[par],weights = 1/temp['%s_STD'%par])
    print('Par: %s\t Val: %.2e'%(par,avg_weighted))
    
    plt.figure(par)
    plt.scatter(metaData['n'], metaData[par])
    plt.errorbar(metaData['n'], metaData[par], yerr=metaData['%s_STD'%par],fmt='none', color = 'black', linewidth = 4, zorder =10)
    plt.plot(metaData['n'],[avg_weighted]*3,color = 'red')
    
plt.figure('Fits')
colors = ['green', 'orange', 'red']
for file in glob.glob('Data\\Fixed\\*'):
    split = file.split('\\')[-1].split('.')[0].split('_')
    
    if not 'C' in split[0]: continue     # Weak Coupling Cuts
    if split[1] == 'P': continue         # Voltage Range Cut
    
    n = int(split[2])
    
    data = pd.read_csv(file, sep = '\t')
    plt.scatter(data['V'],data['Ea'], color = colors[n-1])
    
    E_act_vect = np.vectorize(E_act)
    params = dict(metaData[metaData['n'] == n][['Energy','lambda','cap','A','QWidth','T0','T1']].iloc[0])
    data['thr'] = E_act_vect(data['V'],*list(params.values()))
    
    plt.plot(data['V'],data['thr'], color = colors[n-1])
    
    
    
    
    
    
    
    
    
    
    
    
    