# i控制行,j控制列
print('------------for循环九九乘法表------------')
for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, '×', i, '=', i * j, end='\t', sep='')
    print()

print('------------while循环九九乘法表-----------')
i = 1
while i < 10:
    j = 1
    while j < i + 1:
        print(j, '×', i, '=', i * j, sep='', end='\t')
        j += 1
    print()
    i += 1

print('----------用条件判断把偶数行去除掉---------')
i = 1
while i < 10:
    j = 1
    while j < i + 1:
        if i%2 == 0:
            break
        print(i, '×', j, '=', j * i, sep='', end='\t')
        j += 1
    print()
    i += 1