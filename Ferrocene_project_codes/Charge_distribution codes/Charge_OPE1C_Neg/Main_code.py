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
import N_models    




def fxn(V,A,W):
    return N_models.chargeN(V,A,W) 

vec=np.vectorize(fxn) 

W=.15	
A=0.3	 
V=np.linspace(-2,2, 200) 


Q=vec(V,A,W) 

plt.plot(V,Q)
plt.xlabel('V(V)') 
plt.ylabel('Q(e)') 
plt.title('Charge_distribution_OPE1C_Neg') 
plt.savefig('OPE1C_Charge_distribution') 
plt.show() 

