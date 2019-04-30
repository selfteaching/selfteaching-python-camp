#使用for……in循环输入法打印乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d" % (i,j,i*j), end=" ")
    print(" ")

#使用while循环打印乘法表（去掉偶数行）

a = 1 #定义第一个数值
while a <= 9: #定义第一个数值循环范围
    if a%2 > 0:  #限定条件，打印奇数行
        b = 1  #定义第二个数值
        while b < a+1:  #定义第二个数值循环范围
            print ("%d*%d=%2d" % (a,b,a*b), end=" ")
            b += 1
        print(" ")
    a += 1
