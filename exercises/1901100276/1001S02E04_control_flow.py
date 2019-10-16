for x in range(1,10):
    for y in range(1, x + 1):
        print (y, 'x' ,x, '=', x * y, end='\t', sep='')
    print( )

a = 1
while a <= 9:
    if a % 2 != 0:
        d = 1
        while d < a + 1:
            print(a, "x" ,d,'=',a*d, end='\t', sep='')
            d += 1
        print()
    a += 1
