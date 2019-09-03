numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('开始打印九九乘法表')

for a in numbers[:]:
    for b in numbers[:]:
        if a >= b:
            print(a, "*", b, "=", a * b,end="   ")
    print('\n')

print('开始打印去除偶数行的九九乘法表')
for c in numbers[:]:
    d = 1
    if c % 2 ==1:
        while c >= d:
            print(c, "*", d, "=", c * d,end="   ")
            d += 1
        print('\n')
    c += 1