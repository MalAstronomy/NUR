class maximisation:
    
    def __init__(self,name=""):
        self.name=name
        
    def maximisation(self,func): #a,c,d,b
        a= 10**-4
        b= 5
        R= 1.618
        err= 1e-5
        
        c = b - (b - a) / R
        d = a + (b - a) / R 
        
        while abs(c - d) > err:
            if func(c) > func(d):
                b = d
            else:
                a = c

            c = b - (b - a) / R
            d = a + (b - a) / R

        return (b + a) / 2
    
    def maximisation_(self,func):   #a,c,d,b
        a= 20**-4 
        b= 5
        d= (a+b)/2
        err= 1e-5
        R= 1.61803399
        C= 1- R
        print('im running')
        
        if abs(b-d) < abs(d-a) :
            
            d= d
            c= d - C*(d-a)
            
        else : 
            
            c = d
            d = d + C*(d-a)
            
   
        while (abs(b-a) > err*(abs(c)+abs(d))) : 
            print(a,c,d,b)
            if func(c) > func(d): 
                a=a
                c=c
                d=d
                b= (R*d)+ (C*b) 
        
            else: 
                b= b
                d= d
                c= c
                a= (R*c) + (C*a)
        
        if func(c) > func(d) : 
            xmax= c
            
        else : 
            xmax= d
            
        return xmax
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        