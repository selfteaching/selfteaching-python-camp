#使用for...in循环打印九九乘法表
for x in range(1,10):
    for y in range(1,x+1):
        mul = x * y
        print(x, "*", y, "=", mul, end=" ")
    print()
#使用while循环打印九九乘法表并用条件判断把偶数行去除掉
x = 1
while int(x) <= 9:
    if x % 2 != 0:
        y = 1
        while int(y) <= int(x):
            mul = x * y
            print(x, "*", y, "=", mul, end=" ")
            y = y + 1
        print(" ")
    x = x + 1