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



par=pd.read_csv('Saved_P_All_Ea.txt',sep='\s+')

par=dict(par) 
#print(par)  

X=par['Junc']
Y=par['E']
plt.scatter(X,Y) 
plt.title('E for all junctions') 
plt.ylabel("E") 
plt.savefig("E.png") 
plt.show() 



X=par['Junc']
Y=par['l']
plt.scatter(X,Y) 
plt.title('reorganization energy for all junctions') 
plt.ylabel("lambda") 
plt.savefig("l.png") 
plt.show() 


X=par['Junc']
Y=par['cap']
plt.scatter(X,Y) 
plt.title('capacitive coupling for all junctions') 
plt.ylabel("capacitive_coupling") 
plt.savefig("cap.png") 
plt.show() 

X=par['Junc']
Y=par['W']
plt.scatter(X,Y) 
plt.title('W for all junctions') 
plt.ylabel("W") 
plt.savefig("W.png") 
plt.show() 



X=par['Junc']
Y=par['A']
plt.scatter(X,Y) 
plt.title('A for all junctions') 
plt.ylabel("A") 
plt.savefig("A.png") 
plt.show()
 

