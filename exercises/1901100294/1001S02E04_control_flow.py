for i in range(1,10):
    for j in range(1,i+1):
        print( '%d X %d = %d' % (i,j,i*j),end = '  ' )
    print('\t')


i = 1
while i <= 9 :
    j = 1
    while j <= i:
        print('%d X %d = %d' % (i,j,i*j),end = '  ') 
        j += 1
    print('\t')
    i += 2