for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t',sep='')
    print()       
      
          
i=1 
while i<10:
    j=1
    while j<i+1:
        if i%2==0:
            break
        else:
            print(i,'*',j,'=',i*j,end='\t',sep='')
        j += 1
    if i%2!=0:
        print()  
    i+=1

