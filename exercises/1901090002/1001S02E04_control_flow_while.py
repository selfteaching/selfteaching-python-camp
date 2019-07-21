n=-1
while n<9:
        n +=2
        for x in range(1,n+1):
                if x - n < 0:
                        print(n, 'x', x, '=', n*x, ' ', end ='\t')
                continue
        print(n, 'x', x, '=', n*x, ' ')

        