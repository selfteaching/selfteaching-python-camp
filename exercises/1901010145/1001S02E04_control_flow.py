for i in range(1,10):
     for j in range(1,i+1):
         print("%d*%d=%2d" % (i,j,i*j),end=" ")
     print (" ")
for i in range(1,10):
    for n in range(1,10):
        if n<=i:
            while n*i%2!=0:
                print(str(i),"*",n,"=",i*n,end='\t')
                break
    print("")
