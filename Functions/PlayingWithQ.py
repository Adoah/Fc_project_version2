# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 21:57:44 2021

@author: nickl
"""
from penguins.Model       import Model                        as mod
from penguins.functions   import charge                       as Q
import matplotlib.pyplot  as plt
import numpy as np

V = np.linspace(-10,10,1000)

initpar = {
    'QCenter' : -.6,
    'QWidth' : 0.1 
        }

QMod = mod(Q)
QMod.setParams(initpar)
thr = QMod.returnThry(V)

plt.figure('test')
plt.plot(V,thr)