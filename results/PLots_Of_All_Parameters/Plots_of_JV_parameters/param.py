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



par=pd.read_csv('Saved_P.txt',sep='\s+')

par=dict(par) 

 
X=par['mol']
Y=par['gammaC']
plt.scatter(X,Y) 
plt.title('gammaC for each molecular junction') 
plt.ylabel("gammaC") 
plt.savefig("gammaC.png") 
plt.show() 


X=par['mol']
Y=par['deltaE']
plt.scatter(X,Y) 
plt.title('deltaE for each molecular junction') 
plt.ylabel("deltaE") 
plt.savefig("deltaE.png") 
plt.show() 

X=par['mol']
Y=par['eta']
plt.scatter(X,Y) 
plt.title('eta for each molecular junction') 
plt.ylabel("eta") 
plt.savefig("eta.png") 
plt.show() 


X=par['mol']
Y=par['sigma']
plt.scatter(X,Y) 
plt.title('sigma for each molecular junction') 
plt.ylabel("sigma") 
plt.savefig("sigma.png") 
plt.show() 



