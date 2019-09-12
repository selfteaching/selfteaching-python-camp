for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}'.format(j, i, j*i), end=' ')
    print()
    
i = 1   
while i < 10:
    j = 1
    while j <= i:
        if i % 2 == 0:
            pass
        else:
            print('{}x{}={}'.format(i, j, j*i), end=' ')
        j += 1
    print()
    i += 1
