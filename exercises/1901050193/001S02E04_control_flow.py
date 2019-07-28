for i in range(10): 
    for j in range(1,i+1): 
         print(i,'*',j,'=',i*j,end='\t')
         if i==j:
             print()

i=1
while i in range (10): 
    if i % 2==0:
        print()
    else:
        for j in range(1,i+1): 
            print(i,'*',j,'=',i*j,end='\t')
    i+=1