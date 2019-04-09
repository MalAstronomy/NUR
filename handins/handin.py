import numpy as np
import sys
import matplotlib.pyplot as plt
import random
import h5py

%load_ext autoreload
%autoreload 2

from random_number_generator import random_number_generator
from numerical_integrator import numerical_integrator
from happiness import smiles
from interpolator import interpolator
from linear_equation_solver import linear_equation_solver
from differentiation import differentiation
from sampler import sampler
from haloes import haloes
from maximization import maximisation
from sorting import sorting 
from root import root


##############(1)##############
# a) Poisson distribution

def factorial(x):
    fac=np.double(1)
    for i in np.flip(np.arange(1,x+1),axis=0):
        fac=fac*i
    return fac 

def poisson(lamda,k):
    return (((lamda**k)*np.exp(-lamda))/(factorial(k)))

x=[1,5,3,2.6]
y=[0,10,20,40]

for i in np.arange(4):
    print(poisson(x[i],y[i]))
    
# b) Random number generator     

RNG= random_number_generator()


##############(2)##############

def profile(x,A,a=a,b=b,c=c):
    return A*N_sat*((x/b)**(a-3))*np.exp(-(x/b)**c)

def func(x,a=a,b=b,c=c):
    return profile(x,a,b,c)*4*np.pi*(x**2)

# a) 

N_sat=100
a= (RNG.random_number()*(2.5-1.1))+ 1.1
b= (RNG.random_number()*(2-0.5))+ 0.5
c= (RNG.random_number()*(4-1.5))+ 1.5

integrator= numerical_integrator(xmin=10**-4,xmax=5,N=100000, func=func,a=a,b=b,c=c)
A= N_sat/integrator.simpson()

print(a,b,c,A)
 
# b)     

x= np.log10(np.arange(10**-4,5))
y= [np.log10(profile(10**-4,A)), np.log10(profile(10**-2,A)), np.log10(profile(10**-1,A)), np.log10(profile(1,A)), np.log10(profile(5,A))]
xc= np.log10(np.logspace(np.log10(10**-4),np.log10(5),100))

plt.plot(x,y)
plt.scatter(x,y)

interp=interpolator(x,y,xc)
values= interp.natural_cubic_spline()

plt.plot(x,y,label= 'true')
plt.scatter(x,y)
plt.plot(xc,values, label= 'natural cubic spline')
plt.legend()

# c) 

diff=differentiation(func,b=b,n=100).Ridders()

# d) 

def p(x,func):
    return func(x)/N_sat


plt.plot(np.linspace(0,5,1000),p(np.linspace(0,5,1000),func))
plt.show()

rrx,rry,theta,phi= haloes(func,RNG,p).param()
import pylab as pl

plt.plot(np.linspace(0,5,1000),p(np.linspace(0,5,1000),func))
plt.scatter(rrx,rry)
plt.show()

plt.loglog(np.linspace(0,5,1000),p(np.linspace(0,5,1000),func))
plt.hist(np.log10(rrx),bins=np.logspace(np.log10(10**-4),np.log10(5), 20),rwidth=0.95,alpha=0.3) 
pl.show()

plt.scatter(theta,phi)

haloes(func,RNG,p).family_of_haloes()

# e) 

f= h5py.File('/Users/malavikavijayendravasist/Desktop/courses/NUR/haloes.hdf5','r')
hist_avg=np.zeros(20)
for i in np.arange(1000):
    r=f[str(i)+'/r']
    hist,bin_edges=np.histogram(np.log10(r),bins=np.log10(np.logspace(np.log10(10**-4),np.log10(5),21)))
    #print(hist)
    hist_avg= [h_a+h for h_a,h in zip(hist_avg, hist)]
    
hist_avg= [i/1000 for i in hist_avg]

plt.plot(np.log10(np.linspace(10**-4,5,1000)),p(np.linspace(10**-4,5,1000),func))
plt.bar(bin_edges[:-1],hist_avg,alpha=0.5,width=0.2)
plt.show()

# f) 

y= maximisation().maximisation(func)

def expression(x,func,y): 
        return func(x)-(func(y)/2)
    
plt.plot(np.linspace(10**-4,5,1000), expression(np.linspace(10**-4,5,1000),func,y))

root1=root(expression,func,y,l=10**-4,h=y).bisection()
root2= root(expression,func,y,l=y,h=5).bisection()
print(root1,root2)

# g) 

f= h5py.File('/Users/malavikavijayendravasist/Desktop/courses/NUR/haloes.hdf5','r')
max_bin=np.ndarray([])
for i in np.arange(1000): 
    r=f[str(i)+'/r']
    hist,bin_edges=np.histogram(np.log10(r),bins=np.log10(np.logspace(np.log10(10**-4),np.log10(5),21)))
    max_bin= np.append(max_bin,np.max(hist))


mini=min(max_bin)
maxi=max(max_bin)

plt.hist(max_bin,np.arange(mini,maxi,1), density=True)
lamb=np.mean(max_bin)
plt.plot(np.arange(mini,maxi),[poisson(lamb,k) for k in np.arange(mini,maxi)])
plt.show()

# h) 

A_=[]

for a in np.arange(1.1,2.6,0.1): 
    for b in np.arange(0.5,2.1,0.1):
        for c in np.arange(1.5,4.1,0.1):
            integrator= numerical_integrator(xmin=10**-4,xmax=5,N=100000, func=func,a=a,b=b,c=c)
            A_.append(N_sat/integrator.simpson())




































































