import numpy as np
import scipy.optimize as sco
import scipy.stats as scat
import os
import time

class Model:
    
    def __init__(self, function):
    
        self.originalFunction = function
        self.function = function
        self.time = 0
        self.alg  = 'Manual'
        self.method  = 'None'
     
    
    #%% Setting Parameters
    def setParams(self, parameters, bnds = None, calculatedParams={}, Fixed = None):
    
        if Fixed == None:
            fixed = []
        else:
            if type(Fixed) == dict:
                fixed = Fixed.keys()
            if type(Fixed) == list:
                fixed = Fixed
        
                #Check to make sure that the initial parameters lie inside the bounds
        if not bnds == None:
            for par in bnds.keys():
                if par in fixed: continue
                if parameters[par]<bnds[par][0] or parameters[par]>bnds[par][1]:
                    print('The initial value for %s is outside the bounds given. A number between the bounds is being choosen.'%par)
                    parameters[par] = (bnds[par][0]+bnds[par][1])/2
        self.calculatedParams = calculatedParams
        self.bounds = bnds
        self.initialParameters = parameters.copy()
        self.parameters = parameters.copy()
        
        if not fixed == None:
            self.fixed = fixed
            
            for par in fixed:
                del self.initialParameters[par]
                if type(Fixed) == dict:
                    self.parameters[par] = Fixed[par]
                
                if self.bounds == None: continue
                if par in self.bounds.keys():
                    del self.bounds[par]
            
            def reducedfunc(Xvals,*args):
                for i,par in enumerate(self.initialParameters.keys()):
                    self.initialParameters[par] = args[i]
                    self.parameters[par] = args[i]
                
                return self.originalFunction(Xvals,* self.parameters.values())            
            self.function = reducedfunc
            

    #%% Calculate Function
    def returnThry(self,Xvals, pars=[]):
       
        if len(pars) == 0:
            pars =self.initialParameters.values()
        try:
            Yvals = self.function(Xvals,*pars)
        except:
            func = np.vectorize(self.function)
            Yvals = func(Xvals,*pars)
        return np.array(Yvals)
    
    #%% Calculate Residual
    def residual(self, Xvals, Yvals, pars=[], scale = 'lin', fit=False,
                 mode = 'quiet', save = ''):
        
        Xvals = np.array(Xvals, dtype=np.float64)
        Yvals = np.array(Yvals, dtype=np.float64)
        
        X = Xvals
        if scale == 'lin':
            Y = Yvals
            Ythr = self.returnThry(Xvals, pars)
        elif scale == 'log':
            Y = np.log10(np.abs(Yvals))
            Ythr = np.log10(np.abs(self.returnThry(Xvals, pars)))
        else:
            raise ValueError('Not an appropirate scale')
        
        Err = np.log10(np.sqrt(np.sum(np.subtract(Y,Ythr)**2 )))
        if save:
            self.saveParams(pars, Err, save)    
        if mode == 'verbose':
            if self.counter % 50 == 0:
                totTime = time.gmtime(time.time()-self.time)
                print('Calls: %d\tErr: %.2f\tTime: %s'%(self.counter,Err,time.strftime("%H:%M:%S",totTime)))
            self.counter += 1
        
        minval = np.median(abs(Y))
        if fit and minval < np.sqrt(np.finfo(float).eps):
            Y = Y*1E9
            try:
                Ythr = Ythr*1E9
            except:
                Ythr = Ythr*1E9
        return np.subtract(Y,Ythr)
    
    #%% Calculate StandardError
    def standardError(self, Xvals, Yvals, pars=[], scale = 'lin', fit=False,
                      mode = 'quiet', save = ''):
        
        res = self.residual(Xvals, Yvals, pars, scale, fit, mode = mode,
                            save = save)
        return np.log10(np.sqrt(np.sum(res**2)))
    
    #%% Calculating chi2
    def chi2(self, Xvals, Yvals, scale = 'lin'):
        
        if scale == 'lin':
            Ythr = self.returnThry(Xvals)
            return scat.chisquare(Yvals,Ythr, len(self.parameters))[0]
        elif scale == 'log':
            Yvals = np.log10(np.abs(Yvals))
            Ythr = np.log10(np.abs(self.returnThry(Xvals)))
            return scat.chisquare(Yvals,Ythr, len(self.parameters))[0]
        else:
            raise ValueError('Not a recognized scale')
            
    #%% The Fitting Function
    def fit(self, Xvals, Yvals, scale = 'lin', algorithm = 'LS',method = None, mode = 'quiet', save = ''):     
        self.time = time.time()
        self.alg = algorithm
        self.method  = method
        #%% How will the fit progress? Give updates on the fitting process
        # or be silent? If verbose this is what you get:
        if mode == 'verbose':
            Output = "Fitting with Verbose means that the Error will be"
            Output = Output + " printed to console every 50 calls of the"
            Output = Output + " fitting function, and the data will be saved"
            Output = Output + " to a text file."
            self.counter = 0
            if not save:
                Output = Output + " Since no save location was given. The data"
                Output = Output + " will be saved to  Results//FitResults.txt"
                save = 'FitResults.txt'
            print(Output)
        
        # The three different algorithms each prefer the bounds in a different
        # fromat. Here is where that formating is done.
        bounds = []
        if algorithm == 'LS':
            minfunc = lambda args: self.residual(Xvals, Yvals, args, scale,
                                                 fit = True, mode = mode,
                                                 save = save)
            if not self.bounds:
                bounds=(-np.inf,np.inf)
            else:
                lower = []
                upper = []
                for key in self.bounds.keys():
                    lower += [self.bounds[key][0]]
                    upper += [self.bounds[key][1]]
                bounds = [lower,upper]
        elif algorithm in ['min','diff','basin']:
            minfunc = lambda args: self.standardError(Xvals, Yvals, args, scale,
                                                      fit = True, mode = mode,
                                                      save = save)
            if not self.bounds:
                bounds = None
            else:
                bounds = list(self.bounds.values())
        else:
            raise ValueError('Not a recognized Algorithm')
        
        # Each of these has a default method, if no method is given then the
        # default is used. Otherwise the specified method is used
        pars = list(self.initialParameters.values())
        if not method:
            if algorithm == 'LS':
                result = sco.least_squares(minfunc,x0=pars, bounds = bounds)
            elif algorithm == 'min':
                result = sco.minimize(minfunc,x0=pars, bounds = bounds)
            elif algorithm == 'diff':
                result = sco.differential_evolution(minfunc,bounds = bounds)
            elif algorithm == 'basin':
                result = sco.basinhopping(minfunc,x0=pars)
        if method:
            if algorithm == 'LS':
                result = sco.least_squares(minfunc,x0=pars, bounds=bounds, method = method)
            elif algorithm == 'min':
                result = sco.minimize(minfunc,x0=pars,bounds = bounds, method = method)
            elif algorithm == 'diff':
                result = sco.differential_evolution(minfunc,bounds = bounds)
            elif algorithm == 'basin':
                result = sco.basinhopping(minfunc,x0=pars)
        
        for i,par in enumerate(self.initialParameters.keys()):
            self.initialParameters[par] = result.x[i]
            self.parameters[par] = result.x[i]

    #%% Print fit Results
    def print(self, Xvals, Yvals, save = '', scale = 'lin'):
       
        Err  = self.standardError(Xvals, Yvals, scale=scale)
        
        chi2 = self.chi2(Xvals, Yvals, scale = scale)
        
        output = "\n\033[4mFIT REPORT" + ' '*32+'\033[0m\n'
        if self.time:
            totTime = time.gmtime(time.time()-self.time)
            output = output + "Total Fit Time: %s\n"%(time.strftime("%H:%M:%S",totTime))
        output = output + "Fitting Method: %s %s\n\n" %(self.alg, self.method)
        output = output + "\033[4mParameter\033[0m:\t\t\033[4mValue\033[0m:\n"
        for name in list(self.parameters.keys()):
            if name in self.fixed:
                output = output + "\t%s*\t\t\t%.2e\n" %(name, self.parameters[name])
            else:
                output = output + "\t%s\t\t\t%.2e\n" %(name, self.parameters[name])
        output = output + '*Fixed\n\n'
        output = output + '\033[4mError\033[0m:\n'
        output = output + '\tStandard:\t\t%.2f\n' %Err
        output = output + '\tchi sq  :\t\t%.2e\n\n' % chi2
        
        if not len(self.calculatedParams.keys()) == 0:
            output = output + "\033[4mCalculated Param\033[0m:\t\t\033[4mValue\033[0m:\n"
            for name in list(self.calculatedParams.keys()):
                val = self.calculatedParams[name](self.parameters)
                output = output + "\t%s\t\t\t\t%.2e\n" %(name, val)
        if save:
            output = output + 'Save Location: \'Results/%s\'\n'%save
        output = output + '\033[4m_'*42+'\033[0m\n'
        print(output)
        if save:
            self.saveParams(list(self.initialParameters.values()), Err, save)
    
    def saveParams(self, params, Err, loc):
        
        Temp = self.parameters.copy()
        for i,name in enumerate(self.initialParameters.keys()):
            Temp[name] = params[i]
        
        #filepath = 'Results/%s'%loc
        filepath = './Results/'+loc
        output = ''
        isDir = os.path.isdir('Results')
        if not isDir:
            os.mkdir('Results')
        
        isFile = os.path.isfile(filepath)
        if not isFile:
            for name in Temp.keys():
                output = output + name +'\t'
            output = output +'error'+ '\n'
        for val in Temp.values():
            output = output + '%e\t'%val
        output = output + '%.5f\n'%Err
        f= open(filepath,"a")
        f.write(output)
        f.close()






