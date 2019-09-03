for x in range(1, 10):
    print()
    for y in range(1,10):
        if x >= y:
            print(x, '*', y, '=', x*y, sep='', end='\t' )

a = 1
while a < 10:
    print()
    b = 1
    while b <= a:
        if a % 2 == 0:
            break
        else:
            print(a, '*', b, '=', a*b, sep='', end='\t')
            b +=1
    a +=1
print(end='')