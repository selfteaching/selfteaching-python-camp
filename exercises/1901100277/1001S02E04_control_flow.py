 # 九九乘法表 for ... in ...
for i in range(1, 10):    #1-9,每一个元素 遍历出来一次,共循环9次,rang()函数:包含左边,不包含右边
    for j in range(1, i+1): # i 的值是几 ,就循环几次,
#       print('{}x{}={}\t'.format(j, i, i*j), end='')     #\t 为转义字符 ,table制表符(代表4个空格) ;知识点2 :波波课堂--格式化字符串
        print(f"{i}x{j}={i*j} \t",end='' )     #\t 为转义字符 制表符(4个空格) ;知识点2 :波波课堂--格式化字符串
    
    print()    # 上面运算完了,这一行目前就是换行
 



# while 循环打印九九乘法表并用条件判断把偶数行去除掉
a = 1
# b = 1  
while a <=9 :
    if a%2 != 0 :  
        # 每次循环 b的初始值都必须 是从1 开始判断
        b = 1                                
        while b <=a :
            print(f"{a}X{b}={a*b} ",end="")  # 
            b = b+1
        print()   # 目的就是换行
    a = a+1
