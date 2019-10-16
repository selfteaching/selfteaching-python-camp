for m in range(1,10):
    for n in range(1,m+1):
        if m == n:
            print(m,"*",n,"=",m * n)
        else:
            print(m,"*",n,"=",m * n,end='\t')