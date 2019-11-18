for n in range(1, 10):
    for x in range(1, 10):
        if x < n:
            print(x, '*', n, '=', x*n, end ='\t')
        elif x == n:
            print(x, '*', n, '=', x*n)


a = 1
while a < 10:
    b = 1
    while b < a:
        if a%2 != 0:
            print(b, '*', a, '=', a*b, end = '\t')   
        b += 1
    if b == a and a%2 != 0:    
        print(b, '*', a, '=', a*b)
    a += 1