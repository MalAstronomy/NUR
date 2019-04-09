import numpy as np
class sampler(): 
    def __init__(self,rnx,rny,p,func,name=""):
        self.name=name
        self.p= p
        self.rnx=rnx
        self.rny=rny
        self.func=func
        #print(rnx,rny,p(8,func))
        
    def MCMC(self):
        print('not used')
    def rejection(self): 
        logrny=np.log10(self.rny)
        if logrny< np.log10(self.p(self.rnx,self.func)): 
            return (10**(logrny),self.rnx)
        else: return (None,None)