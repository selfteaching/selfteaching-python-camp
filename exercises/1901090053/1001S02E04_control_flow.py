for i in range(1, 10):
    for j in range(1, i+1):
        result = 1*j
        print('{}*{}={}'.format(i, j, result), end='\t')
    print()      

i = 1
while i<10:
    if i%2!=0:
        j=1
        while j<i+1:
            result = i*j
            print('{}*{}={}'.format(i, j, result), end='\t')
            j+=1
        print()     
    i+=1
    