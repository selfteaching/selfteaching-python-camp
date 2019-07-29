#使用 for。。。in循环打印九九乘法表
for i in range(1,10):    # for循环语句,给i赋值
    for j in range(1,i+1):
        print('{}*{}={}\t'.format(i,j,i*j), end = ' ')    
        # end取消输出回车符，实现不换行
        # end = ' '增加空格
    
    print()



#使用while循环打印舅舅乘法表表，并用条件判断把偶数行除掉


    
for i in range(1, 10):
    while i % 2 == 0:
        break
    
    else:
        for j in range(1, i+1):
            print('{}*{}={}\t'.format(j, i, i*j), end='')
    print()