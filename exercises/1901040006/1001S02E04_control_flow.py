
#使用for循环打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i,'*', j, '=', i * j, end = '\t')
    print()

print('\n')
    
#使用while循环打印奇数行九九乘法表
i = 1
while i < 10:
    if i % 2 == 1:
        for j in range(1, i + 1):
            print(i,'*', j, '=', i * j, end = '\t')
        print()
    i = i + 1
    
