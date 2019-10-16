#用for in 循环打印九九乘法表
for i in range (1,10):
    for j in range (1,i+1):
        x = int(i)
        y = int(j)
        z = int(i*j)
        if i > j:
            print(f'{x}*{y}={z}',end='\t')
        if i == j:
            print(f'{x}*{y}={z}',end='\n')
#用while循环打印九九乘法表,并去除偶数行
a = 1
while int(a)<10:
    if a%2==1:
        b = 1
        c = a*b
        while int(b)<=int(a):
            print(f'{a}*{b}={c}', end='\t')
            b = b+1
        print()
    a=a+1        