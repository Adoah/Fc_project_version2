from math import *
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  
from scipy.integrate import quad,dblquad
from scipy import integrate
import datetime 
import csv
from scipy.optimize import minimize
from scipy.optimize import differential_evolution 
import glob 
import random 
#from New_Class import Model 
import models    
from F4 import Fitting 





     
  
def fxn(vb, gammaL, gammaR, deltaE, eta,gauss):
    n = 1 
    I = models.tunnelmodel_1level_nogate_300K_gauss(vb, gammaL, gammaR, deltaE, eta,gauss) 
    return np.log10(abs((n *I) /2.41E-06)) 
   
ipar = {
        
	'gammaL'   :5.639812e-04,	
	'gammaR'   :1.862810e-02,	
	'deltaE1'  :7.0e-01,	
	'eta'      :4.905496e-01, 	
	'sigma'    :1.50000e-01	
	}    


bnds = {
    'gammaL'  : [0,1],
    'gammaR'  : [0,1],
    'deltaE1' : [0.6999999,0.71],
    'eta'     : [0,1],
    'sigma'   : [0.14999,0.151] 
      } 
 
  
    
    
 

data =pd.read_csv('OPEn.txt', delimiter = '\t',header=None) 
data1 = data[abs(data[0])>0] 
#print(data1) 

rawD={
          'X':data1[0],
          'Y':data1[1]       
          }
 
 

     
Obj=Fitting(fxn,rawD) 


Obj=Fitting(fxn,rawD)
Obj.Fit(bnds,ipar)
Obj.PrintFit()
plt.scatter(Obj.workD['X'],Obj.workD['Y'],label='Exp data',color='black')  

plt.plot(Obj.modelD['X'],Obj.modelD['Y'],label='Fitted curve',color='red') 
#plt.yscale('log')
plt.xlabel("voltage(V)") 
plt.ylabel("|J|(A/cm^2)")   
plt.title("OPE1")
plt.savefig("sigma_1.5.png")   
plt.legend() 
plt.show() 
 











































































   
