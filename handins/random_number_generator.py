class random_number_generator: 
    
    def __init__(self,seed=45,name=""): 
        self.name= name
        self.seed=seed
    
    def MLCG(self,I,a= 3935559000370003845, c= 2691343689449507681, m = (2**64)-1): # ; a=1664525,c=1013904223,m=2**32 a= 123456788957, c= 65432109857, m = (2**32)-1
        return ((((a*I)+c) % (m)))

    def SFbit(self,x,a1=21,a2=35,a3=4):
        mask= (2**64-1)
        x= int(x)
        x ^= (x>>a1) & mask
        x ^= (x<<a2) & mask
        x ^= (x>>a3) & mask
        return x/mask
    
    def combine_random(self):
        x= self.MLCG(self.seed)
        x= self.SFbit(x)
        self.seed=x
        return x
    
    def random_number(self):    
        return (self.combine_random())
    
    def hist(self):
        y=[]
        x=[]
        z=[]
        for i in np.arange(1000):
            x.append(self.seed)
            y.append(self.random_number)
            self.seed= y[:-1]
        plt.hist(y,bins=10)
        plt.show()