#乘法表 用for in and while

def multiply_for(n):
    for d in range(1,n+1):
        for e in range(1,d+1):
            print(d,'*',e,'=',d*e,end='\t')
        print()

def multiply_while(n):
    a=1
    while a<=n:
        b=1
        while b<=a:
            print(a,'*',b,'=',a*b,end='\t')
            b=b+1
        print()
        a=a+2

multiply_for(9)
multiply_while(9)