#使用for...in循环打印出九九乘法表
print("使用for...in循环打印出九九乘法表")
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end="  ")
    print("")

print("")

#使用while循环打印九九乘法表并用条件判断把偶数行去掉
print("使用while循环打印九九乘法表并用条件判断把偶数行去掉")
i = 1 #定义变量i
while i < 10:  #判断条件
    if i % 2 ==0: #判断i是否是偶数，是偶数则加1
        i += 1
    j = 1  #定义变量j
    while j < i+1:  #判断j小于i
        print(i,"*",j,"=",i*j,end="  ") #打印结果
        j += 1
    i += 1
    print("")



