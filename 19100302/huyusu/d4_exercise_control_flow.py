for x in range(1,10):  
    for y in range(1, x+1):
        print('{}x{}={}\t'.format(x, y, x * y), end='')
    print('\n')



x = 1
while x <= 9:
    y = 1
    while y <= x:
        if x % 2 == 0:
            break
        print("%d * %d = %d\t" % (x,y,x*y),end="")
        y += 1
    print()
    x += 1
