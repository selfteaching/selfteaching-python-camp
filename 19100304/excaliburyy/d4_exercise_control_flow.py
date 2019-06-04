for i in range(1,10):
    for x in range(1,i+1):
        print( '%d X %d = %2d' % (i ,x ,i*x) ,end = '  ' )
    print('  ')

a = 1
while a < 10:
    if a%2 == 1:
        for b in range(1,a+1):
            print( '%d X %d = %2d' % (a,b,a*b), end = '  ')
        print(' ')
    a = a+1