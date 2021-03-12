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

DataFile1 = 'Data//OPEn_Positive_volts.txt'   # This is Ea for OPEn, n=1,2,3. it has a voltage range {0.2,1.0)    
DataFile2 = 'Data//OPEn_Negative_volts.txt'   # This is Ea for OPEn, n=1,2,3. it has a voltage range {-1.0,-0.2)  
data = pd.read_csv(DataFile2, delimiter = '\t',header=None)  
data1 = data[abs(data[0])>0] 
c=data1.dropna()
 

x=c[0] # this column is the voltage 
y1,y2,y3=(c[1],c[2],c[3])  # These columns are Ea for OPE1,OPE2,OP3 respectively 

plt.scatter(x,y1) 
plt.show() 

""" 
ipar = {
        
	'E'    :0.75,	
	'l'    :1.0687,	
	'cap'  :4.209971e-19 ,
	'W'    :3.489849e-01	, 
	'A'    :0.25	
	

        }  
        

      

       'E'    :8.042445e-02,	
	'l'    :1.068756e-01,	
	'cap'  :4.209971e-01 ,
	'W'    :3.489849e-01	, 
	'A'    :-1.349318e+00	
	


bnds = {
    'E'     : [-1,1],
    'l'     : [0,1.5],
    'cap'   : [0,1],
    'W'     : [-1,1],
    'A'     : [-1.5,1.5]  
      } 
 
 
cols=[1]    


for col in cols: 
    print(col) 
    rawD={
          'X': c[0],
          'Y': c[col] 
          }
      
    def fxn(V,E,l,cap,W,A):
        return models.nitzanmodel_fixedtemp_biasvoltage(V,E,l,cap,W,A)
    
    Obj=Fitting(fxn,rawD)
    Obj.Fit(bnds,ipar)
    Obj.PrintFit()
    
    plt.scatter(Obj.workD['X'],Obj.workD['Y'],color='black')   

    plt.plot(Obj.modelD['X'],Obj.modelD['Y'],color='red') 
    plt.xlabel("voltage(V)") 
    plt.ylabel("E_a")   
    plt.title("Ea_OPE1_{0.2,1.2}")
    plt.savefig("Ea_OPE1_{0.2,1.2}.png")    
#plt.legend() 
plt.show()

""" 





















































   
