for i in range (1,10):
    for j in range(1,10):
        print(j,"x",i,"=",i*j,"\t",end="")
        if i==j:
            print()
            break