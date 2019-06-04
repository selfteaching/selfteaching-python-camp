for i in range(1,10):
    for j in range(1,i+1):
        d = i * j
        print('%d*%d=%-2d'%(i,j,d),end = ' ' )
    print()



    i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%-2d"%(i,j,i*j),end = ' ')
        j += 1
    print()
    i += 1