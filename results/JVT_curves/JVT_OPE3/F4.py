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


class Fitting:
      def __init__(self,eqn,rawD):
          self.eqn=eqn
          self.rawD=rawD
          self.model=np.vectorize(eqn)
          self.workD=self.rawD.copy()
          self.param={}
          self.err={} 
          self.modelD={} 
      def __fit(self,model,pb,pi):
          p0=[]
          l_b=[]
          u_b=[]
          bnds=[]
          for key in list(pb.keys()):
              p0+=[pi[key]]
              l_b+=[pb[key][0]]
              u_b+=[pb[key][1]]
          bnds=[l_b,u_b]
          X=self.workD['X']
          Y=self.workD['Y']
          res,cov=curve_fit(model,X,Y,p0=p0,bounds=bnds)
          return res,cov
      def Fit(self,pb,pi):
          res,cov=self.__fit(self.model,pb,pi)
          self.modelD['X']=self.workD['X']
          self.modelD['Y']=self.model(self.workD['X'],*res)
          i=0
          for key in list(pb.keys()):
              self.param[key]=res[i]
              self.err[key]=np.sqrt(np.diag(cov))[i]
              i+=1
      def CRE(self,pi):
          X=self.workD['X']
          Y=self.workD['Y']
          Ythr=self.model(X,*pi.values())
          resi=np.subtract(np.log(np.abs(Y)),np.log(np.abs(Ythr)))
          Err=np.sqrt(np.sum(resi**2))
          return Err
      def PrintFit(self,*args):
          Err=self.CRE(self.param)
          out="Fit_report:\tError\t%.2f\n"%Err
          out=out + "\tpar:\tval\tErr\n"
          for name in list(self.param.keys()):
              out=out+ "\t%s\t%e\t%e\n"%(name,self.param[name],self.err[name])
          print(out) 
                
                
                  
          
