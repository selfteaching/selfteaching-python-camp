i = 1
while i < 10:
    j = 1
    while j<=i:
        print('{}x{}={}\t'.format(i, j, i*j), end='')
        j=j+1
    print('')
    i = i + 2
