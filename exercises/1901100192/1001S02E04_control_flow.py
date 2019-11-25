

for n in range(1, 10):
    for m in range(1, n+1):
        print("%d*%d=%2d" % (n,m,n*m), end ="   ")
    print()

    n = 1
while n <= 9:
    m = 1
    while m <= n:
        if n % 2 > 0: 
            print("%d*%d=%d\t" % (n, m, n*m),end='')
        m += 1
    if n % 2 != 0: 
        print()    
    n += 1


