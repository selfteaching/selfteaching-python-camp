#for i in  range(1,10):
#    for j in  range(1,i+1):
#        print("%d*%d=%d" %(i,j,i*j),end=" ")
#    print('\n')
i = 0
while (i < 10):
    j = 1
    while (j < i+1):
        if (i % 2 == 1):
            print("%d*%d=%d" %(i,j,i*j),end=" ")  
        j += 1
    i += 1
    if (i % 2 == 1):
        print('\n')



