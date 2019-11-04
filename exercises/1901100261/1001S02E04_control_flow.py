print('打印九九乘法表')
for a in range(1,10):
    for b in range(1,a+1):                #第二个 for ，循环第是第二个乘数 y，当第二个乘数小于第一个乘数 +1时，遍历一遍。
        print(a,'*',b,'=',a*b,end='\t')   #此 print 函数属于第二个 for 循环
    print()                              #此 print 函数属于第二个 for 循环，在末尾换行。

#空行来分隔下一个代码
pass
print('\n打印去除偶数列的九九乘法表')   #打印去除偶数列的九九乘法表
for i in range(1,10,2):              #本来想用要求的 while 语句来排除偶数，突然想起 rang 的第3个量可以表示有序数列的间隔
    for m in range(1,i+1):           #只需要设置 i 的变量为奇数
        print(i,'*',m,'=',i*m,end='\t')  #或 print("{} * {} = {}".format(i, j, i*j),end="\t") 
    print()

#空行分隔代码
pass
print('\n打印去除偶数列的九九乘法表')   #打印去除偶数列的九九乘法表,使用 while 函数
for x in range(1,10):
    while x % 2 == 0:   #先判断值，去除偶数后进行下面的语句，结果为True，就停止
        break           #之前总是有一行空的，反复以为是break 的问题，后来发现其实是最后一行的 print的位置出了问题
    else:
        for y in range(1,x+1):     
            print("{} * {} = {}".format(x, y, x*y), end='\t')
        print()      #原本将print写在了else下，打印出来总是有个空行，翻看上面第代码，这个语句应该是在第2个for之下
    