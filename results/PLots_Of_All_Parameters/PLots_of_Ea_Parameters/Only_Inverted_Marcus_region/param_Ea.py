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



par=pd.read_csv('Saved_P_Ea.txt',sep='\s+')

par=dict(par) 
#print(par)  
 
X=par['Junc']
Y=par['E']
plt.scatter(X,Y) 
plt.title('E for inverted Marcus region') 
plt.ylabel("E") 
plt.savefig("E.png") 
plt.show() 


X=par['Junc']
Y=par['l']
plt.scatter(X,Y) 
plt.title('reorganization energy for inverted Marcus region') 
plt.ylabel("lambda") 
plt.savefig("l.png") 
plt.show() 


X=par['Junc']
Y=par['cap']
plt.scatter(X,Y) 
plt.title('capacitive coupling for inverted Marcus region') 
plt.ylabel("capacitive_coupling") 
plt.savefig("cap.png") 
plt.show() 

X=par['Junc']
Y=par['W']
plt.scatter(X,Y) 
plt.title('W for inverted Marcus region') 
plt.ylabel("W") 
plt.savefig("W.png") 
plt.show() 

X=par['Junc']
Y=par['A']
plt.scatter(X,Y) 
plt.title('A for inverted Marcus region') 
plt.ylabel("A") 
plt.savefig("A.png") 
plt.show() 

