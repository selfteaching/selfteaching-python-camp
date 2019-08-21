for i in range(1, 10):
    for j in range(1, i+1):
        print('{}×{}={}'.format(j, i, i*j), end='\t')
    print()
    
    i = 1
while i < 10:
    j = 1
    while j<=i:
        if i%2 == 0:
           break
        print('{}*{}={}'.format(i,j,i*j),end='\t')
        j +=1
    i +=1
    print()
    