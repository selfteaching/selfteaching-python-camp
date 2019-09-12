#for...in循环九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, '*', j, '=', i * j,end='\t')
    print()
    
#while循环九九乘法表
x = 1
while x <= 9:
    if x % 2 != 0:
        y = 1
        while y < x + 1:
            print(x, '*', y, '=', x * y,sep=' ',end='\t')
            y += 1
        print()
    x += 1