i=0
while i <10:
    i+=1
    if i%2 ==0:
        continue
    for j in range(1, i+1):
            print('{}x{}={}\t'.format(i, j, i*j), end='')
    print()