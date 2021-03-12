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

gl=np.array([9.872764e-04,9.949335e-04,3.471600e-03,1.199909e-02,2.885358e-02])
gr=np.array([1.000328e-03,1.124890e-03,3.483758e-03,1.199909e-02,2.884609e-02]) 

gammaC=np.array([9.87600227e-07, 1.11919074e-06 ,1.20942143e-05, 1.43978161e-04,8.32312966e-04]) 

gammaW=np.array([0.0019876,  0.00211982, 0.00695536 ,0.02399818 ,0.05769967]) 
Capital Gamma=[0.00049688, 0.00052796, 0.00173883 ,0.00599955, 0.01442492]   
deltaE1=[4.3,3.6,2.6,2.2,1.7] 
