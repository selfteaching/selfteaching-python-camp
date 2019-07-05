for i in range (1,10):
    for j in range(1,10):
        print(i,"x",j,"=",i*j,"\t",end="")
        if i==j:
            print("")
            break


for i in range(1, 10):
    if i % 2 != 0:
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(i, j, i*j),end='')
        print()


print()
