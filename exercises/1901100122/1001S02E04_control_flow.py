print('打印九九乘法表')
for i in range(1, 10):                                      #行数1-10，不包括10
    print('第%d行' % i, end='\t')                           #打印行数
    for j in range(1, i + 1):                               #列数1- i+1 ,不包括 i+1
        #print(i, '*', j, '=', i * j, end='\t')             #第一种打印方法，end='\t'意思是结束时自动加TAB
        print('{} * {} = {}'.format(i, j, i * j), end='\t') #第二种打印方法，end='\t'意思是结束时自动加TAB
    print()                                                 #换行

print('\n打印跳过 偶数 行的九九乘法表')
i = 1                                                               #行数开始等于1
while i < 10:                                                       #当行数小于10的时候
    if i % 2 == 0:                                                  #取模运算，就是计算两个数相除之后的余数，符号是%。
        print()                                                     #换行
    else:
        print('第%d行' % i, end='\t')                               #打印行数
        for j in range(1, i + 1):                                   #列数
            print(i , '*', j, '=', i * j, end='\t')                 #第一种打印方法，end='\t'意思是结束时自动加TAB
            #print('{} * {} = {}'.format(i, j, i * j), end='\t')    #第二种打印方法，end='\t'意思是结束时自动加TAB
    i += 1                                                          #循环完毕i+1

print('\n打印跳过 奇数 行的九九乘法表')
i = 1                                                               #行数开始等于1
while i < 10:                                                       #当行数小于10的时候
    if i % 2 != 0:                                                  #取模运算，就是计算两个数相除之后的余数，符号是%。
        print()                                                     #换行
    else:
        print('第%d行' % i, end='\t')                               #打印行数
        for j in range(1, i + 1):                                   #列数
            print(i, '*', j, '=', i * j, end='\t')                  #第一种打印方法，end='\t'意思是结束时自动加TAB
            #print('{} * {} = {}'.format(i , j, i * j), end='\t')   #第二种打印方法，end='\t'意思是结束时自动加TAB
    i += 1                                                          #循环完毕i+1