for n in range(1,10):
    for m in range(1,n+1):
        print(n,"*",m,"=",n*m, end='\t')
        if n == m:
            print()


for n in range(1,10):
    m = 1
    if n % 2 != 0:
        while m <= n:
            print(n, "*", m, "=", n * m,end="\t")
            m += 1
        print('\n')