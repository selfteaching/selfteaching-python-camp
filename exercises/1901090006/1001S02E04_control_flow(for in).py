def multiply(x,y):
    return x*y

for i in [1,2,3,4,5,6,7,8,9]:
    for j in range(1,i+1):
        print(i,'*',j,'=',multiply(i,j),end='\t')
    print()