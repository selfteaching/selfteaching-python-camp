i = 1
while i <10:
    j = 1
    while j<=i:
        if i%2 == 0:
            break
        print('{}*{}={}\t'.format(i,j,i*j),end='')
        j+=1
    print()
    i +=1