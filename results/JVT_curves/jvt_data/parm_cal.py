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


 
par=pd.read_csv('parameters.txt',sep='\s+') 
par=dict(par) 

X=par['mol']
Y=par['Gamma']
plt.scatter(X,Y) 
#plt.yscale("log")

plt.ylabel("Capital gamma") 
plt.title("Capital gamma")

plt.show()  






























































 

"""
x1=dat['voltage'] 
y1=dat['C14H']
x11=Thry['voltage']
y11=Thry['C14H']

x2=dat['voltage'] 
y2=dat['C14F']
x22=Thry['voltage']
y22=Thry['C14F']

x3=dat['voltage'] 
y3=dat['C14Cl']
x33=Thry['voltage']
y33=Thry['C14Cl']

x4=dat['voltage'] 
y4=dat['C14Br']
x44=Thry['voltage']
y44=Thry['C14Br']

x5=dat['voltage'] 
y5=dat['C14I']
x55=Thry['voltage']
y55=Thry['C14I']

plt.scatter(x1,y1, label="C14H")
plt.plot(x11,y11, 'r')

plt.scatter(x2,y2, label="C14F")
plt.plot(x22,y22, color="green")

plt.scatter(x3,y3, label="C14Cl")
plt.plot(x33,y33, color="yellow")

plt.scatter(x4,y4, label="C14Br")
plt.plot(x44,y44, color="blue")

plt.scatter(x5,y5, label="C14I")
plt.plot(x55,y55, color="black")


plt.set_title("All molecules")
plt.set_xlabel("voltage/v")
plt.set_ylabel("log(J)/A/cm2") 
plt.legend(loc="lower left") 


    
 
 
fig,(ax1,ax2)=plt.subplots(nrows=2,ncols=1,sharex=True)
#plt.figure("gammaC")
X=par['mol']
Y=par['gammaC']
ax1.scatter(X,Y) 
ax1.set_yscale("log")

ax1.set_ylabel("gammaC") 
#ax1.set_title("gammaC")
 

#plt.figure("deltaE")
X=par['mol']
Y=par['deltaE']
ax2.scatter(X,Y) 

ax2.set_ylabel("deltaE") 
#ax2.set_title("deltaE")
plt.show() 




X=par['mol']
Y=par['Gamma']
ax1.scatter(X,Y) 

ax1.set_ylabel("Gamma") 
#ax1.set_title("Gamma=(gammaL*gammaR)/(gammaL+gammaR)")


X=par['mol']
Y=par['gammaW']
ax2.scatter(X,Y) 

ax2.set_ylabel("gammaW") 
#ax2.set_title("gammaW=gammaL+gammaR")
plt.show() 
"""

