#使⽤ for...in 循环打印九九乘法表

for o in range(1,10): #定义外层循环(行数)
        for i in range(1,10): #定义内层循环（）列数
                if (i <= o): #条件判断
                        print(o,'*',i,'=',i*o,end='   ') #打印乘法表
        print(' ')#控制换行


#使⽤ while 循环打印九九乘法表并⽤条件判断把偶数⾏去除掉

o = 1 #定义行的初始值
while o <= 9:#定义行的范围
        i = 1#定义列的初始值
        while i <= o and o % 2 != 0:#定义列的范围并且定义去除偶数行的方法
                print(o,'*',i,'=',i*o,end='   ')#打印乘法表
                i += 1 #像for循环那样列自增1
        print('')#控制换行
        o += 1#行数自增1


# t = 1
# while t <= 9:
#     if t % 2 != 0:
#         s = 1
#         while s < t + 1:#  t + 1 →2？那再
#             print(t,"*",s,"=",t*s,end=" ")
#             s += 1
#         print()
#     t += 1



