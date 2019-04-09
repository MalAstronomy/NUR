class linear_equation_solver:
    def __init__(self,name=""):
        self.name=name
        
    def gauss_jordon(A,b):           
        n=len(A)
        M=np.copy(A)
    #     print(M)
        M=np.append(M,b,axis=1)
        print(M)
        for i in np.arange(n):
            p= np.argmax(np.abs(A[i:,i]))
            print(i,p)
            if (A[p][i]==0):        #singular 
                continue 
            elif A[p][i]> A[i][i]:
                M[[p,i]]=M[[i,p]]   #exchange rows  
            else:
                pass

            M[i]=M[i]/M[i][i]
            for j in np.arange(i+1,n):  #reducing to echelon form 
                M[j]-= M[j][i]*M[i]

        s= M[:,3]
        M=M[:,:3]

        #print(s)
        print(M)