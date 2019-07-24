#python 用for循环打印九九乘法表：
print("1.for循环打印九九乘法表")
for i in range (1,10):
    #对于1到9的所有整数都带入i这个变量，执行一遍以下任务：
    for j in range(1,10):
        print(j,"*",i,"=",i*j,"\t",end="")
        #（在运算符前后和逗号后使用空格，但不能直接在括号内使用）
        if i==j:
            print("")
            break

#while循环打印九九乘法表，用条件判断把偶数行去掉
print('2.while循环打印九九乘法表，用条件判断把偶数行去掉')
i=1#赋值为1
j=1
while(i<=9):
    while(i%2 !=0):
        #当i除以2的余数不等于零，执行下面的语句：
        while(j <=i):
            print(i,'*',j,'=',i*j,'\t',end='')
            j=j+1
        else:
        #循环结束时，执行以下语句
            print(end='\n')
        break
        #跳出最近的while循环
    i=i+1
    j=1
        