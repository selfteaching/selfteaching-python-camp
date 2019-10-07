
print('打印九九乘法表')
for i in range(1, 10):# 从第1行循环到第9行
    print('第%d行' % i, end='\t')# 打印行号
    for j in range(1, i+1):# j从1循环到i+1
        print(i,'*',j,'=',i*j,end='\t')# 打印乘法算式，并空8个字符
        # print('{}x{}={}\t'.format(j, i, i*j), end='\t')
    print()# 结束打印

print('打印去除偶数行的九九乘法表')
i = 1
while i<10:#while是条件判断循环
    if i%2==0:# 如果i是奇数
        print()# 不打印
    else:
        for j in range(1, i+1):
            print(i,'*',j,'=',i*j,end='\t')
    i += 1

print('九九乘法表01')
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
print('\n')


print('九九乘法表02')
row = 1 # 行号
while row<= 9:
    col = 1 # 列号
    while col<=row:
        print("%d*%d=%d" %(col,row,col*row), end='\t')
        col += 1
    print('')
    row += 1
print('\n')

print('九九乘法表（除去偶数行）')
for i in range(1,10):
    if i % 2 == 0 :
        i += 1 
        continue
    for j in range(1,i+1):
            print('{}x{}={}\t'.format(i,j,i*j),end='')
    print('')
