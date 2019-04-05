#用for...in编九九乘法表
for i in range(1,10): 
     for j in range(1,i+1): 
         print(i,'*',j,'=',i*j,end='\t')
         if i == j: 
             print()
print()

#用while编去偶数行的九九乘法表
i=0
j=0
while i<9:
    i+=1
    if i%2==0:
        continue
    while j<9:
        j+=1
        print(i,'*',j,'=',i*j,end='\t')
        if i==j:
            j=0
            print()
            break 