i = 1
while i < 10:
    j = 1
    while j<=i:
        print('{}*{}={}'.format(i,j,i*j),end='\t')
        j += 1
    i += 2
    print()
    