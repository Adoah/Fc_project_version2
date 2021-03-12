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



DataFile1 = 'Data//OPEnC_Positive_volts.txt'   # This is Ea for OPEnC, n=1,2,3. it has a voltage range {0.2,1.2)    
DataFile2 = 'Data//OPEnC_Negative_volts.txt'   # This is Ea for OPEnC, n=1,2,3. it has a voltage range {-1.0,-0.2)  
DataFile3 = 'Data//Positive_SM.txt'   # This is Ea for OPEnC, n=1,2,3. it has a voltage range {0.2,1.2) 
DataFile4 = 'Data//sm3.txt'   # This is Ea for OPEnC, n=1,2,3. it has a voltage range {0.2,1.2)
data = pd.read_csv(DataFile2, delimiter = '\t',header=None)  
data1 = data[abs(data[0])>0] 
c=data1.dropna()
 
#print(c) 

#x_OPE1C,y_OPE1C=(c[0],c[1])  
#x_OPE2C,y_OPE2C=(c[2],c[3]) 
x_OPE3C,y_OPE3C=(c[4],c[5])  

#plt.scatter(x_OPE1C,y_OPE1C)
#plt.scatter(x_OPE2C,y_OPE2C)
#plt.scatter(x_OPE3C,y_OPE3C)
#plt.show() 

 
ipar = {        	
	'E'   :	-1.050553e-01,	
	'l'   :	1.923315e-01,
	'cap' :	1.000000e+00,	
	'W'   :	5.792358e-01, 	
	'A'   :	-5.099990e-01	
      }   
   
        
bnds = { 
     'E'     : [-1,1],  
    'l'     : [0,1.5],
    'cap'   : [0,1],
    'W'     : [-1,1],
    'A'     : [-1,1] 
      } 


rawD={
          'X': c[4],
          'Y': c[5]       
          }
      
def fxn(V,E,l,cap,W,A):
    E_a=models.nitzanmodel_fixedtemp_biasvoltage(V,E,l,cap,W,A)
    
    return np.abs(1*E_a)   
    
Obj=Fitting(fxn,rawD)
Obj.Fit(bnds,ipar)
Obj.PrintFit()
    
plt.scatter(Obj.workD['X'],Obj.workD['Y'],color='black')  

plt.plot(Obj.modelD['X'],Obj.modelD['Y'],color='red') 
plt.xlabel("voltage(V)") 
plt.ylabel("E_a(meV)")   
plt.title("Ea_OPE3C_{-1.0,-0.2}") 
plt.savefig("Ea_OPE3C_Fixed_{-1.0,-0.2}.png")    
#plt.legend() 
plt.show()

















































   
