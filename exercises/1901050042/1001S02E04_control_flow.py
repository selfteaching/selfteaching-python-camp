for row in range(1, 10):
    for col in range(1, row+1):
        print('{}*{}={}'.format(col, row, col * row), end='\t')
    print()



i=1#行控制
while i<=9:
    j = 1#列控制
    while j<=i:
        if i % 2 == 0:
            break
        print("%dx%d=%d"%(i,j,i*j),end=' ')
        j=j+1
    print(' ')
    i+=1