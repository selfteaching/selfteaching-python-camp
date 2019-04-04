print(end='\n')
n = 1
while n <= 9 : 
    if (n % 2 !=0):
        i = 1
        while i <= n :
            if (i % 2 !=0 ):
                print ("%d * %d = %d" %(n,i,n*i),end='\t')
    
