import numpy as np

class sorting:
    
    def __init__(self,b,name):
        self.name=name
        self.b=b
        self.c=np.empty(len(self.b))   

    def mergeSort(self):
        
        if len(self.b) == 1: 
            return self.b

        else: 

            h= int(len(self.b)/2)
            lh= self.b[:h]
            mergeSort(lh)
            mergeSort(rh)

            k=0
            while (len(lh) > 1) and (len(rh) > 1) :
                if lh[0] < rh[0]:
                    self.c[k]=(lh[0])
                    lh.pop(0)    
                else:
                    self.c[k]=(rh[0])
                    rh.pop(0)
                k+=1    

            while len(lh) > 1 :
                self.c[k]=lh[0]
                lh.pop(0)
                k+=1

            while len(rh) > 1:
                self.c[k]=rh[0]
                rh.pop(0)
                k+=1
            
            return self.c

    

