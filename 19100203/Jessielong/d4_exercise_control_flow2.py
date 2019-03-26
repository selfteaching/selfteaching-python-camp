#是去掉偶数行，不是去掉所有偶数；可以再做一次
i=0
j=0
while i<9:
    i+=1
    while j<9:
        j+=1
        if i%2==0 or j%2==0:
            print()
        else:
            print(j,"x",i,"=",i*j,"\t",end="")
        
        if i==j:
            j=0
            print("")
            break


