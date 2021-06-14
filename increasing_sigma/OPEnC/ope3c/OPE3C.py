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




def fxn(vb, gammaL, gammaR, deltaE, eta,sigma): 
    n = 100 
    I = models.tunnelmodel_1level_nogate_300K_gauss(vb, gammaL, gammaR, deltaE, eta,sigma)    
    return np.log10(abs((n *I) /2.41E-06)) 
   
ipar = { 
	
	
	
	'gammaL'    :7.562759e-04, 
	'gammaR'    :5.770550e-06,	
	'deltaE1'   :8.776013e-01,	
	'eta'       :6.22e-01,	
	'sigma'     :2.000000e-01	
	


       }   
   


bnds = {
    'gammaL'  : [0,1],
    'gammaR'  : [0,1],
    'deltaE1' : [0,1],
    'eta'     : [0,1],
    'sigma'   : [0.2,1]       
      } 
 
  
        

data =pd.read_csv('ForCURVES.txt', delimiter = '\t',header=None) 
data1 = data[abs(data[0])>0] 


rawD={
          'X':data1[0],
          'Y':data1[5]     
          }


i='Theory_X_data' 
j='Theory_Y_data'  
All=pd.DataFrame() 
Obj=Fitting(fxn,rawD) 


Obj=Fitting(fxn,rawD)
Obj.Fit(bnds,ipar)
Obj.PrintFit()
plt.scatter(Obj.workD['X'],Obj.workD['Y'],label='Exp data',color='black')  

plt.plot(Obj.modelD['X'],Obj.modelD['Y'],label='Fitted curve',color='red') 
All['%s'%i]=Obj.modelD['X'] 
All['%s'%j]=Obj.modelD['Y']  
All.to_csv('HE.txt',sep='\t')  
plt.xlabel("voltage(V)") 
plt.ylabel("|J|(A/cm^2)") 
plt.title("OPE3C(n=100)") 
plt.savefig("OPE3C.png")   
plt.legend() 
plt.show()  
 





































































   
