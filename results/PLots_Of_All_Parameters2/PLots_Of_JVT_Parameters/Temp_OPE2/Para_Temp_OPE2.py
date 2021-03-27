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



par=pd.read_csv('Tem_OPE2.txt',sep='\s+')

#par=dict(par) 
#print(par)  


X=par['par']
Y=par['gL']
plt.scatter(X,Y) 
plt.title('gammaL for Temp_OPE2') 
plt.ylabel("gammaL") 
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0)) 
plt.ylim(1e-03,1e-01)  
plt.savefig("gL.png") 
plt.show() 


X=par['par']
Y=par['gR']
plt.scatter(X,Y) 
plt.title('gammaR for Temp_OPE2') 
plt.ylabel("gammaL") 
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0)) 
plt.ylim(1e-03,1e-01) 
plt.savefig("gR.png") 
plt.show() 

X=par['par']
Y=par['gW']
plt.scatter(X,Y) 
plt.title('gammaW for Temp_OPE2') 
plt.ylabel("gammaW") 
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0)) 
plt.ylim(1e-03,1e-01)  
plt.savefig("gW.png") 
plt.show() 

X=par['par']
Y=par['deltaE']
plt.scatter(X,Y) 
plt.title('deltaE for Temp_OPE2') 
plt.ylabel("gammaL") 
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0)) 
plt.ylim(0,1) 
plt.savefig("deltaE.png") 
plt.show() 


X=par['par']
Y=par['eta']
plt.scatter(X,Y) 
plt.title('eta for Temp_OPE2') 
plt.ylabel("eta") 
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0)) 
plt.ylim(0,1) 
plt.savefig("eta.png") 
plt.show() 

X=par['par']
Y=par['sigma']
plt.scatter(X,Y) 
plt.title('sigma for Temp_OPE2') 
plt.ylabel("sigma") 
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0)) 
plt.ylim(0.01,0.5) 
plt.savefig("sigma.png") 
plt.show() 

X=par['par']
Y=par['gC']
plt.scatter(X,Y) 
plt.title('gammaC for Temp_OPE2') 
plt.ylabel("gammaC") 
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0)) 
plt.ylim(1e-05,1e-03) 
plt.savefig("gC.png") 
plt.show() 




