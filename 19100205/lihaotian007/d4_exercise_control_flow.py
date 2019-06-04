#ֵ使用for/while循环打印九九乘法表，while循环需要剔除偶数的行
a = 0 #创建整数型变量
b = 0 #创建整数型变量
x = input('请选择控制结构[for/while]' '\n') #选择控制结构
if x == 'for': #选择控制结构为for循环时使用
    for a in range(1,10): #外层for循环1-9，控制行数
        for b in range(1,a):      #内层for循环1-a-1,控制列数
            print(a,'*',b,'=',a*b,end='\t') #输出非最后一列的值，中间用制表符隔开
        print(a,'*',b+1,'=',a*(b+1)) #输出最后一列的值，用换行符换行
elif x == 'while': #选择控制结构为while时使用
    while a <= 9 : #外层while循环1-9
        if a % 2 != 0 : #在a不为偶数时进入
            while b < a :  #内层while循环，1-a-1
                print(a,'*',b,'=',a*b,end='\t') #输出非最后一列的值，中间用制表符隔开
                b += 1
            print(a,'*',b,'=',a*b) #输出最后一列的值，用换行符换行
        a += 1
        b = 1 #控制b在进入内层循环的值