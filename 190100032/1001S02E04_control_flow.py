
print('打印九九乘法表')
for x in range(1,10):
    print("第%d行" % x, end='\t') 
    for y in range(1, x+1):
        print(x, '*', y, '=', x * y, end='\t')
    print()
    
print('\n打印跳过偶数行的九九乘法表')
x = 1
while x < 10:
    if x % 2 == 0:
        print()
    else: 
        for y in range(1, x + 1):
            print(x, '*', y, '=', x * y, end='\t')
    x +=1

print('\n打印跳过奇数行的九九乘法表')
x = 1
while x < 10:
    if x % 2 == 1:
        print()
    else:
        for y in range(1, x + 1):
            print(x, '*', y, '=', x * y, end='\t')
    x +=1

print('\n打印1到10质数的九九乘法表')
for x in range(2, 10):
    for n in range(2, x):
        if x % n == 0:
            print()
            break
    else:
        for y in range(2, x + 1):
            print(x, '*', y, '=', x * y , end='\t')
    x +=1


