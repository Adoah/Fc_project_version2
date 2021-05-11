from math import *
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt  
from scipy.integrate import quad,dblquad
from scipy import integrate 
import csv
from scipy.optimize import minimize
from scipy.optimize import differential_evolution   
import N_models    



def  fxn(Vg,E,l):  
     T0=298
     T1=300  
     return N_models. E_act_fixedtemp_gatevoltage(Vg,E,l,T0,T1) 
vecComp = np.vectorize(fxn) 

E=0.7
l=0.15 
	   
Vg=np.linspace(-1.2,0.2,500)  
 
I=vecComp(Vg,E,l)    
plt.plot(Vg,I,color='blue',label='OPE3C')





def  fxn(Vg,E,l):  
     T0=190
     T1=300
     return N_models. E_act_fixedtemp_gatevoltage(Vg,E,l,T0,T1) 
vecComp = np.vectorize(fxn) 

E=0.7
l=0.15 	
	   
Vg=np.linspace(-1.2,0.2,500)  
 
I=vecComp(Vg,E,l)    
plt.plot(Vg,I,color='green',label='OPE2C')

def  fxn(Vg,E,l):  
     T0=55
     T1=400
     return N_models. E_act_fixedtemp_gatevoltage(Vg,E,l,T0,T1) 
vecComp = np.vectorize(fxn) 

E=0.7 
l=0.15	   
Vg=np.linspace(-1.2,0.2, 500)  
 
I=vecComp(Vg,E,l)    
plt.plot(Vg,I,color='red',label='OPE1C') 
plt.xlabel('Vg(V)') 
plt.ylabel('Ea(meV)') 
plt.title('Ea_vs_Vg for OPEnC_Neg') 
plt.legend() 
plt.show() 

