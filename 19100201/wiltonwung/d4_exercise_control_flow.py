print("九九乘法表")#标题
print("-"*100)#分隔符
for a in range(1,10):#乘数9以内的数字
    for b in range(1,10):#被乘数也是
        print(a,"*",b,"=",a*b,end='\t')#循环打印乘法列表
        if a == b:#一旦到达两个数字相同的时候
            print("")#分行
            break#重新开始下一个数字的如此循环
print("-"*100)#分隔符



print("奇数乘法表")
print("-"*100)
a = 1   #a的初始值指定为1

while a<10: #a的最大为9
    if a%2 == 0:    #判断如果a是偶数
        a = a + 1  #就把a变成奇数
    b = 1   #b的初始值也指定为1
    while b<a+1:    #开始乘法
        print(a,'*',b,'=',a*b,end='\t') #打印列表
        b = b + 1#a乘以b一直循环到比到自己为止
    print('') #换行
    a = a + 1 #a从1开始一直到9
print("-"*100)#分隔符
