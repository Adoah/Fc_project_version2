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



ipar = { 
	
	'gammaL'   :1.181429e-01,	
	'gammaR'   :1.181429e-01,	
	'deltaE1'  :8.878924e-01, 	
	'eta'      :9.999987e-01,
	'sigma'    :5e-01	
	
       }     

#'sigma'  :5.000397e-03	
bnds = {
    'gammaL'  : [0,1],
    'gammaR'  : [0,1],
    'deltaE1' : [0,1],
    'eta'     : [0,1],
    'sigma'   : [0,1]  
      } 
 
  
    
data =pd.read_csv('JVT_OPE3C.txt', delimiter = '\t',header=None)  
data1 = data[abs(data[0])>0]

#print(data1) 
 


  
cols=[1,2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17,18,19] 
#cols=[1]   
#cols=[1]  
for col in cols:
    print(col) 
    rawD={
          'X': data1[0],
          'Y': data1[col] 
          }
           

    #plt.plot(rawD['X'],rawD['Y'])           
    Temp=[0,270,260,240,230,220,210,200,190,180,170,160,150,140,130,120,110,100,80,50]   

    def fxn(vb, gammaL, gammaR, deltaE1, eta,sigma):
        
        c  = 0
        vg = 0
        T  = Temp[col] 
        n = 3000
        
        gammaC = gammaL*gammaR
        gammaW = gammaL+gammaR
        I = models.tunnelmodel_singleLevel(vb,gammaC,gammaW, deltaE1,eta,sigma,c,vg,T) 
        return n*I
    
    Obj=Fitting(fxn,rawD)
    Obj.Fit(bnds,ipar)
    Obj.PrintFit()
    
    plt.scatter(Obj.workD['X'],Obj.workD['Y'],color='black')  

    plt.plot(Obj.modelD['X'],Obj.modelD['Y'],color='red')
plt.xlabel("voltage(V)") 
plt.ylabel("|J|(A/cm^2)")   
plt.title("Temp dependent of OPE3C")
plt.savefig("JVT_OPE3C.png")    
#plt.legend() 
plt.show()
 




































































   
