for n in range(1,10):
    for x in range(1,n+1):
        if x - n < 0:
            print(n, '*', x, '=', n*x, ' ', end ='\t')
            continue
        print(n, 'x', x, '=', n*x, ' ')  
