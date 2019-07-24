# for循环九九乘法表

for i in range(1, 10):
    for j in range(1, 10):
        print(i, 'x', j, '=', i*j,'\t', end='') #end=''表示不换行
        if i == j:
            print('')
            break 


# while 循环九九乘法表并用条件判断把偶数行去除掉

x = 1
y = 1
while(x < 10):
    while(x % 2 != 0):
        while(y <= x):
            print(x, 'x', y, '=', x*y,'\t', end='' )
            y = y + 1
        else:
            print(end = '\n')
        break
    x = x + 1
    y = 1