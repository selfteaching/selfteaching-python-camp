# Day4 控制流程

# 使用 for...in 循环打印九九乘法表

i = int(1)
x = int(1)

print('九九乘法表')
for i in range (1, 10):
    print('第',i,'行', end='\t')
    for x in range (1, i+1):
        print(x, 'x', i, '=', x*i, end='\t')
    print()

#结束

print()

#使⽤用 while 循环打印九九乘法表并⽤用条件判断把偶数⾏行行去除掉


i = int(1)
x = int(1)

print('奇数⾏九九乘法表')
while (i < 10):
    if i % 2 == 0:
        print()
    else:
        print('第',i,'行', end='\t')
        for x in range (1, i+1):
            print(x, 'x', i, '=', x*i, end='\t')
    i += 1

