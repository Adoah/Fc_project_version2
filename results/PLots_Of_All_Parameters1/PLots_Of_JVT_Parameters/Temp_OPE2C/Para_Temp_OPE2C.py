from math import *
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.optimize import differential_evolution 
from scipy.optimize import minimize 
import matplotlib.pyplot as plt
from scipy.integrate import quad,dblquad
from scipy import integrate
from time import time 
import csv



par=pd.read_csv('Tem_OPE2C.txt',sep='\s+')

#par=dict(par) 
#print(par)  


X=par['par']
Y=par['gL']
plt.scatter(X,Y) 
plt.title('gammaL for Temp_OPE2C') 
plt.ylabel("gammaL") 
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0)) 
plt.ylim(2e-02,6e-02) 
plt.savefig("gL.png") 
plt.show() 


X=par['par']
Y=par['gR']
plt.scatter(X,Y) 
plt.title('gammaR for Temp_OPE2C') 
plt.ylabel("gammaR") 
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0)) 
plt.ylim(2e-02,6e-02)  
plt.savefig("gR.png") 
plt.show() 

X=par['par']
Y=par['deltaE']
plt.scatter(X,Y) 
plt.title('deltaE for Temp_OPE2C') 
plt.ylabel("deltaE") 
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0)) 
plt.ylim(0.5,1.0) 
plt.savefig("deltaE.png") 
plt.show() 


X=par['par']
Y=par['eta']
plt.scatter(X,Y) 
plt.title('eta for Temp_OPE2C') 
plt.ylabel("eta") 
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0)) 
plt.ylim(0.50,1) 
plt.savefig("eta.png") 
plt.show() 

X=par['par']
Y=par['sigma']
plt.scatter(X,Y) 
plt.title('sigma for Temp_OPE2C') 
plt.ylabel("sigma") 
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0)) 
plt.ylim(0.01,0.3) 
plt.savefig("sigma.png") 
plt.show() 

X=par['par']
Y=par['gC']
plt.scatter(X,Y) 
plt.title('gammaC for Temp_OPE2C') 
plt.ylabel("gammaC") 
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0)) 
plt.ylim(5.0e-04,9.0e-03)  
plt.savefig("gC.png") 
plt.show() 




