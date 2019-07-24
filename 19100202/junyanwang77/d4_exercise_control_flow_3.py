i = 1
while i < 10:
    j = 1
    while j<=i:
        if i%2 == 0:
           break
        print('{}*{}={}'.format(i,j,i*j),end='\t')
        j += 1
    i +=1
    print()
    
    