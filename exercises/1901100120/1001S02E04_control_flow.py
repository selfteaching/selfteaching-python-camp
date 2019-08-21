for n in range(1, 10):
    for i in range(1,n+1):
          print (i,'*',n,'=',i*n,end='\t')
          if i == n:
              print(' ',)
        
i = 1
j = 1
while (i<10): 
    if i%2!=0:           
         print (i,'*',j,'=',i*j,end='\t')    
         j += 1
         if (j > i) :
           i += 1
           j = 1
           print(' ')
    else:
          i += 1