for i in range (1,10):
    for j in range (1,i+1):
            print('%d*%d=%2d\t'%(i,j,i*j),end='')
    print()


for i in range(1,10):
    while i%2==0:
        break
    else:
        for j in range(1,i+1):
            print('%d*%d=%2d\t'%(i,j,i*j),end='')
    print()
print()

