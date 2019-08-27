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