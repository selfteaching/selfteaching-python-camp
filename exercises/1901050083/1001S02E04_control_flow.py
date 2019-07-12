# for...in 循环打印九九乘法表
for a in range(1,10):
    for b in range(1,a+1):
        print(a,"*",b,"=", a*b, end='\t')
        if b==a:
            print()

# while循环打印九九乘法表
a = 1 
while a <= 9:
    if  a % 2 != 0:
        b = 1
        while b <= a:
            print(a,"*",b,"=", a*b, end='\t')
            if b==a:
                print()
            b=b+1
    a=a+1



        