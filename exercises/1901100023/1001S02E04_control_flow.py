
print('打印九九乘法表')
for i in range (1, 10):           #遍历一个从1～9的列表，不包含10。i可以理解为行
    print('第%d行' % i, end='\t') # control+斜杠 可以注释掉
    for j in range(1, i + 1):    # j可以理解为列
        print(i, '*', j, '=', i * j, end='\t')
        # print('{}*{}={}'.format(i,j,i*j), end='\t')
        # end='\t'表示以tad键结尾（空格符号-占8个字符位）
    print()

print('\n打印跳过偶数行的九九乘法表')
i = 1  # ‘=’是赋值的意思，把i的起始值设为1
while i < 10:
    if i % 2 == 0:  # %取余数
        print()  #就换行～
    else:        #否则就执行
        for j in range(1, i + 1):
            print(i, '*', j, '=', i * j, end='\t')
    i += 1  # 是i=i+1 的缩写，相当于把上一个的i再加1，重新赋值给了新的i