#使用for...in循环打印九九乘法表
for cnt in range(1, 10):
    num1 = cnt
    for num in range(1, cnt+1):
        num2 = num
        print(f'{num1}*{num2}={num1*num2}', end = '\t')
    print()

#使用while循环打印九九乘法表的奇数行
n = 10
a = 1

print()

while(a < n):
    n1 = a
    if(n1%2 != 0):
        print()
        b = 1
        while(b < n1 + 1 and n1%2 != 0):
            n2 = b        
            print(f'{n1}*{n2}={n1*n2}', end = '\t')
            b = b + 1
    a = a + 1