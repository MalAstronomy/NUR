#!/usr/bin/env python3

import numpy as np

class numerical_integrator:
    
    def __init__(self,xmin,xmax,N,func,a,b,c, name=""):
        
        self.name=name
        self.xmin=xmin
        self.xmax=xmax
        self.N=N
        self.func=func
        self.a=a
        self.b=b
        self.c=c
        
    def trapezoid(self):
        h=(self.xmax-self.xmin)/self.N
        return h*((self.func(self.xmin)+self.func(self.xmax))/2 + np.sum(self.func(np.linspace(self.xmin+h,self.xmax,N)))) 

    def simpson(self):
        h=(self.xmax-self.xmin)/self.N
        return (h*((self.func(self.xmin,a=self.a,b=self.b,c=self.c)+self.func(self.xmax,a=self.a,b=self.b,c=self.c))/3 + (np.sum(self.func(np.linspace(self.xmin+h,self.xmax,self.N) [1::2],a=self.a,b=self.b,c=self.c)*4) + np.sum(self.func(np.linspace(self.xmin+h,self.xmax,self.N)[2::2],a=self.a,b=self.b,c=self.c)*2))/3))



    