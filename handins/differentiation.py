
import numpy as np

class differentiation: 
    
    def __init__(self,func,b,n,name=""): 
        self.b=b
        self.n=n
        self.func=func
        self.name=name
     
    def Ridders(self): 
        a= np.empty((self.n,self.n))
        ans= np.empty((self.n,self.n))
        h=0.1
        x=self.b
        a[0][0]= (self.func(x+h)-self.func(x-h))/(2*h)
        c=1.4
        c2=c*c
        safe=2.0
        err= 1e30
        
        for i in np.arange(1,self.n): 
            h/= c
            a[0][i]= (self.func(x+h)-self.func(x-h))/(2*h)
            fac=c2
            for j in np.arange(1,i+1): 
                a[j][i]=(a[j-1][i]*fac-a[j-1][i-1])/(fac-1.0)
                fac=c2*fac
                errt=max(abs(a[j][i]-a[j-1][i]),abs(a[j][i]-a[j-1][i-1]))
                
                if (errt <= err): 
                    err=errt
                    ans=a[j][i]
            if (abs(a[i][i]-a[i-1][i-1]) >= (safe*err)): 
                break
                
        return ans