print("九九乘法�?�?")
for i in range(1,10,1):
    # print(i,end= ' ')
    for j in range(1,i):
        #����д����print('%d*%d=%d' %(i,j,i*j),end= ' ' )
         print('%d*%d=%d' %(i,j,i*j),end= ' ' )

    print("")
for i in range(1,10,2):
    # print(i,end= ' ')
    for j in range(1,i+1):
        print('%d*%d=%d' %(i,j,i*j),end= ' ' )
    print("")
