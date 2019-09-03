for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,sep='',end='\t')
    print()


i=1
while i<10:
    if i%2!=0:
        j=1
        while j<=i:
            print(i,'*',j,'=',i*j,sep='',end='\t')
            j+=1
        else:
            pass
        print()
    i+=1
    
    



        
