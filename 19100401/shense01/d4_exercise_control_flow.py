for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print("")



i = 1
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    j = 1
    while j <= i:
        print('%d*%d=%-2d'%(j,i,j*i),end=' ')
        j += 1
    print()
    i += 1
