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
print(gl) 

