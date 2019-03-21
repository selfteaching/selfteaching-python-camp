for i in range(0,10):
    print()
    for j in range(1,i+1):
        result = int(i)*int(j)
        print(i,'*',j,'=',result,end='\t')

    
for i in range(0,10):
    if i%2 ==0:
        continue
    print()
    for j in range(1,i+1):
        result = int(i)*int(j)
        print(i,'*',j,'=',result,end='\t')
             