for i in range(1, 10):
    for j in range(1,i+1):
        k=i*j
        print(i,"*",j,"=",k,'\t',end="")
    print('\t')

i=1
while i<10:
    j=1
    while j<=i:
        print("%d*%d=%-2d"%(i,j,i*j),'\t',end="")
        j+=1
    print()
    i+=2