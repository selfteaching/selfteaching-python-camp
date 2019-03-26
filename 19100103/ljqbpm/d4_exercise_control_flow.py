#使用for、while打印九九乘法表

def multiply_for(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,'*',j,'=',i*j,end='\t')
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