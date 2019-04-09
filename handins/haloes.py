import h5py
import numpy as np
from sampler import sampler

class haloes:
    
    
    def __init__(self,func,RNG,p,name=""):
        self.name=name
        self.func=func
        self.RNG=RNG
        self.p=p
        
    def param(self):
        rry=[]
        rrx=[]
        theta=[]
        phi=[]
        r=[]

        while len(rry)<100:
            rnx= self.RNG.random_number()*5
            rny= self.RNG.random_number()*50
            #print(rnx,rny)
            ry,rx= sampler(rnx,rny,self.p,self.func).rejection()
            if ry==None and rx==None: continue
            else: 
                rry.append(ry)
                rrx.append(rx)

            #print(len(rry))
        for i in np.arange(100):
            theta.append(self.RNG.random_number()*(2*np.pi))
            phi.append(np.arccos(1-2*self.RNG.random_number()))
        return (rrx,rry,theta,phi)
        
        
    def family_of_haloes(self): 

        f= h5py.File('/Users/malavikavijayendravasist/Desktop/courses/NUR/haloes.hdf5','w')
        for i in np.arange(1000):

            rrx,rry,theta,phi=self.param()
            s= f.create_group(str(i))
            s1=s.create_dataset('r',data= rrx)
            s2=s.create_dataset('theta',data=theta)
            s3=s.create_dataset('phi',data=phi)

        f.close()