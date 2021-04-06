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
from Old_Class import Fitting 





def fxn(V,E,l,cap,W,A):
    Ea=models.nitzanmodel_fixedtemp_biasvoltage(V,E,l,cap,W,A)
    return Ea  


   
ipar = {
        'E'    :-7.5e-01,	
	'l'    :1.2e+00,
	'cap'  :1.2,	
	'W'    :0.26, 	
	'A'    :0.83	
        } 



bnds = {
    'E'       : [-0.751,-0.749],
    'l'       : [1.19,1.5],
    'cap'     : [0,1.5],
    'W'       : [0.25,1],
    'A'       : [0,0.84]       
         } 
 
  
    
    


DataFile = 'Data//20180426.txt'
data = pd.read_csv(DataFile, delimiter = '\t',header=None) 
 


   
rawD={
          'X':data[0],
          'Y':data[1]  
          }
         

Obj=Fitting(fxn,rawD)
Obj.Fit(bnds,ipar)
Obj.PrintFit()
plt.scatter(Obj.workD['X'],Obj.workD['Y'],label='Exp data',color='black')  
plt.plot(Obj.modelD['X'],Obj.modelD['Y'],label='Fitted curve',color='red') 
plt.xlabel("voltage(V)") 
plt.ylabel("E_a(meV)")     
plt.legend() 
plt.savefig("Act_Energy.png",dpi=720) 
plt.show() 

 









































































   
