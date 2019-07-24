for i in range(1,10):
    for j in range(1,i+1):
           print('%d*%d=%2d\t'%(j,i,i*j),end="")
    print()
        
            
            

i=0
j=0
while i<9:
    i+=1
    while j<9:
        j+=1
        print(j,"x",i,"=",i*j,"\t",end="")
        if i==j:
            j=0
            print("")
            break
    
       
       



i=1#行控制
while i<=9:
   
    j = 1#列控制
    
    while j<=i:
        
        print("%dx%d=%d"%(i,j,i*j),"\t",end="")
       
        j=j+1
    
    print("")
    
    i+=2
