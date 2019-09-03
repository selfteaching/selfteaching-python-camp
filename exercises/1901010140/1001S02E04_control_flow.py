#方案一：利用for...in 实现九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
          print('%d*%d=%2d\t'%(j,i,i*j),end='')#%d指的是整型
    print()
#方案二：利用for...in 实现九九乘法表
for i in range(1,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j,"\t",end='')#end=""表示不换行
        if i == j:
            print("")
            break
#方案三:利用for...in +format函数实现九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={} ".format(i,j,i*j),end="")#format函数是一种格式化输出字符串的函数（str.format）,基本语法是通过｛｝和：来代替以前的%。
    print()
#方案四：利用while实现九九乘法表
i=0
j=0
while i<9:
    i+=1
    while j<9:
        j+=1
        print(i,"x",j,"=",i*j,"\t",end="")
        if i==j:
            j=0
            print("")
            break
#使用 while 循环打印九九乘法表并用条件判断把偶数行去除掉01
i=1
while i<10:
    j=1
    while j<=i:
        if i%2==0:
            break
        print('{}*{}={} '.format(i,j,i*j),end="") 
        j += 1
    print()
    i +=1
#使用 while 循环打印九九乘法表并用条件判断把偶数行去除掉02
i=1
while  i < 10:
    if i % 2 == 0:
        print()
    else:
        for j in range(1,i+1):
            print(i,'*',j,'=',i*j,end='\t')
    i += 1