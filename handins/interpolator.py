import numpy as np



class interpolator:
    
    def __init__(self,x,y,xc,name=""):
        self.name=name
        self.x= x
        self.y= y
        self.xc=xc

   
    def knots(self,x,y):
        M=np.zeros((len(self.x)-2,len(self.x)-2))
        b=np.zeros((len(self.x)-2,1))

        for i in np.arange(1,len(self.x)-1): 
#             print('i',i)
            for j in np.arange(1,len(self.x)-1): 
#                 print('j',j)
                if i==j: 
                    M[i-1][j-1]= 2*(x[i-1]-x[i+1])

                elif j==i+1: 
                    M[i-1][j-1]= x[i]-x[i+1]

                elif j==i-1: 
                    M[i-1][j-1]= x[i-1]-x[i]

                else:                              #if (j> i+1 or j<i-1)
                    M[i-1][j-1]= 0

            b[i-2] = 6* (((y[i-1]-y[i])/(x[i-1]-x[i]))- ((y[i]-y[i+1])/(x[i]-x[i+1])))


        #knots= linear_equation_solver().gauss_jordon(M,b)  
        knots= np.linalg.solve(M,b)
        return knots
                    
    def f(self,xc,x,y): 

        k= self.knots(x,y)
        k=np.reshape(k,np.shape(k)[0])
        k=np.append(k,0)
        k=np.insert(k,0,0)

        a=x[xc>=x][-1]
#         print('x',x)
#         print('a',a)
        i= np.where(x==a)[0][0]
        if i< 4 : 
            ff = ((k[i]/6)*(((xc-x[i+1])**3/(x[i]-x[i+1])) - ((xc-x[i+1])*(x[i]-x[i+1]))) - 
        (k[i+1]/6)*(((xc-x[i])**3/(x[i]-x[i+1])) - ((xc-x[i])*(x[i]-x[i+1]))) + 
        ((y[i]*(xc-x[i+1])- y[i+1]*(xc-x[i]))/(x[i]-x[i+1])))
            
        else: 
            i=3
            ff = ((k[i]/6)*(((xc-x[i+1])**3/(x[i]-x[i+1])) - ((xc-x[i+1])*(x[i]-x[i+1]))) - 
        (k[i+1]/6)*(((xc-x[i])**3/(x[i]-x[i+1])) - ((xc-x[i])*(x[i]-x[i+1]))) + 
        ((y[i]*(xc-x[i+1])- y[i+1]*(xc-x[i]))/(x[i]-x[i+1])))
            
        return ff   

    
    def natural_cubic_spline(self):
        x=self.x
        y=self.y
        
#         y=[]
#     #putting x in ascending order
#         l = list(enumerate(x))
#         l= np.sort(l)                              #(#######################################)
#         x,indices = zip(*l)  #this x is sorted
#         y.append(self.y[i] for i in indices) #this y is sorted 

        values=[]
        for i in self.xc: 
            #print(i)
            values.append(self.f(i,x,y))
            
        return values
        
    
        
        
        