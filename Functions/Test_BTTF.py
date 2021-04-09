import glob
import pandas as pd
import matplotlib.pyplot  as plt
from penguins.Model       import Model                        as mod
from penguins.functions   import E_act_fixedtemp_biasvoltage  as E_act
import numpy as np

Fixed = {
    # 'Energy' : -0.85,
    # 'lambda' : 0.82,
    # 'cap'    : 1.78,
    # 'AWidth' : -0.85,
    # 'QWidth' : 0.53,
    'T0'     : 298,
    'T1'     : 300
    }
    
initpar = {
    'Energy' : -0.85,
    'lambda' : 0.82,
    'cap'    : 1.78,
    'AWidth' : -0.85,
    'QWidth' : 0.53,
    'T0'     : 298,
    'T1'     : 300
    }

bnds = {
    'Energy' : [-1,1],
    'lambda' : [-1,1],
    'cap'    : [-1,2],
    'QWidth' : [-1,1],
    'AWidth' : [-1,1],
    'T0'     : [0,400],
    'T1'     : [0,400]
        } 

for file in glob.glob('Data\\BTTF*.txt'):
    
    data = pd.read_csv(file, sep = '\t')
    
    EaModel = mod(E_act)
    EaModel.setParams(initpar,Fixed=Fixed, bnds = bnds)
    EaModel.fit(data['V'],data['Ea'], algorithm = 'LS', mode = 'verbose')
    EaModel.print(data['V'],data['Ea'])
    # newEntry['Err']= EaModel.standardError(data['V'],data['Ea'])
    data['thr'] = EaModel.returnThry(data['V'])
    # x   = np.linspace(-1,0.5,100)
    # thr = EaModel.returnThry(x)
    
    plt.figure('BTTF')
    plt.scatter(data['V'],data['Ea'], color = 'black')
    plt.plot(data['V'],data['thr'], color='red')
    # plt.plot(x,thr)
    