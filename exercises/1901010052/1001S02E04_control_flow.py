# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='') # 格式
    print()


# 九九乘法表去掉偶数行
i = 1
while i <= 9:
    j = 1
    while j <= i and i % 2!=0:
        print('{}*{}={}'.format(i,j,i*j),end = " ")  # \t往右边移动一个制表符位
        j += 1
    print()
    i += 1
    