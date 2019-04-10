#for...in语句生成九九乘法表
for a in range(1, 10):
    for b in range(1, a+1):
        print('{}*{}={}\t'.format(a, b, a*b), end='')
    print()

# while循环生成九九乘法表
row = 1
while row <= 9:
    column = 1
    while column <= row:
        print('%d*%d=%d\t' %(column, row, row*column), end= '')
        column += 1
    print()
    row += 1

# while循环取九九乘法表奇数行
row = 1
while row <= 9:
    column = 1
    while column <= row:
        print('%d*%d=%d\t' %(column, row, row*column), end= '')
        column += 1
    print()
    row += 2