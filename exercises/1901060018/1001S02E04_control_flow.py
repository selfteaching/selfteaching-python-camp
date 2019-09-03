#for与while解题思路相同
#先做每一横行：x不变，y从1~x
#再做纵行：x从1~9
#把总行套在横行外面既完成整个循环
#组合使用for和range函数
#让x从1循环到9
for x in range(1, 10):
    #y从1循环到x
    for y in range(1, x+1):
        #定义num等于x乘以y
        num = x * y
        #打印x + y =num,不换行
        print(x, "*", y, "=",num, end='\t')
    #打印完一整横行后，换行
    print(" ")

#初始值a = 1,在竖行中递增
a = 1
while int(a) <= 9:
    #判断a是否为奇数
    if a % 2 != 0:
        #初始值b = 1,在每一横行中递增
        b = 1
        #while函数，当某个条件满足时执行
        while int(b) <= int(a):
            num = a * b
            print(a, "*", b, "=", num ,end='\t')
                #初始值b = 1,在每一横行中递增
            b = b + 1
        print(" ")
    #初始值a = 1, 一行行递增
    a = a + 1

    
