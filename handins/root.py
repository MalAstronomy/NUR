class root:
    def __init__(self,expression,func,y,l,h,name=""):
        self.name=name
        self.func=func
        self.expression=expression
        self.y=y
        self.l=l 
        self.h=h
    
    def bisection(self):
        tol= 1e-5
        l=self.l
        h=self.h
        c= l 
        while ((abs(self.expression(c,self.func,self.y)) > 0.01) or (abs((h-l))/2 > tol)): 

            if (self.expression(l,self.func,self.y)*self.expression(h,self.func,self.y)) < 0: 
                c= (l+h)/2

                if self.expression(l,self.func,self.y)*self.expression(c,self.func,self.y) <0 : 
                    h= c
                else : 
                    l= c 
                    
        return c    
                
                    