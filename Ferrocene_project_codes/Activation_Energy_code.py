from math import *
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit,least_squares 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  
from scipy.integrate import quad,dblquad
from scipy import integrate
import csv
from scipy.optimize import minimize
from scipy.optimize import differential_evolution 
import random 
from scipy import stats 
from time import time 
from scipy.interpolate import interp1d 
import glob
from N_class import Model    as mod
import N_models  
import os 


Fixed = {
    # 'E' : -0.85,
    # 'l' : 0.82,
    # 'cap'    : 1.78,
    # 'A' : -0.85,
    # 'W' : 0.53,
    'T0'     : 298,
    'T1'     : 300
    }

initpar = {
    'E'     : -0.85,
    'l'     : 0.82,
    'cap'   : 1.78,
    'A'     : -0.85,
    'W'     : 0.53,
    'T0'    : 298,
    'T1'    : 300
    }

bnds = {
    'E'     : [-1,1],
    'l'     : [-1,1],
    'cap'   : [-1,2],
    'W'     : [-1,1],
    'A'     : [-1,1],
    'T0'    : [0,400],
    'T1'    : [0,400]
        } 



def fxn(V,E,l,cap,A,W,T0,T1):
    return N_models.E_act_fixedtemp_biasvoltageP(V,E,l,cap,A,W,T0,T1) 
 
metaData = pd.DataFrame()
colors = ['green', 'orange', 'red'] 

for file in glob.glob('OriginalData/*.txt'): 
    newEntry = {}
    split = file.split('/')[-1].split('.')[0].split('_') 
    newEntry['mol']     = split[0]
    newEntry['V range'] = split[1] 
    newEntry['n']       = int(split[2]) 
    newEntry['FileName'] = split = file.split('/')[-1].split('.')[0] 
    
    data = pd.read_csv(file, sep = '\t') 
    print(newEntry['FileName'])
    Object = mod(fxn)
    Object.setParams(initpar,Fixed=Fixed, bnds = bnds) 
    Object.fit(data['volt'],data['Ea'],save = '%s.txt'%newEntry['FileName'], algorithm = 'basin', mode = 'verbose')
    Object.print(data['volt'],data['Ea'],save = '%s.txt'%newEntry['FileName']) 
    params = Object.parameters
    newEntry['Err']= Object.standardError(data['volt'],data['Ea'])
    data['thr'] = Object.returnThry(data['volt']) 
    
    #Plotting Eact vs Bias and saving figure
    plt.figure('Eact Vs Bias %s' %newEntry['mol'])
    plt.scatter(data['volt'],data['Ea'], color=colors[newEntry['n']-1], label = 'n == %d'%newEntry['n'])
    plt.plot(data['volt'],data['thr'], color=colors[newEntry['n']-1])
plt.savefig('All.png', dpi=720)     
plt.show() 
    
    
    
