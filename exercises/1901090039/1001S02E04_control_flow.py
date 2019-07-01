#使⽤ for...in 循环打印九九乘法表
for i in range(1,10):
        for j in range(1,i+1):                                #内层循环
                print("{}*{}={}".format(i,j,i*j),end=" ")
        print("")


#使用while循环打印九九乘法表并用if条件将偶数去掉
i = 1
while i<=9:
    j = 1
    while j<=i:
        if (i%2) == 0:
                break
        print("{}*{}={:<2}".format(i,j,i * j),end = " ")
        j += 1
    i += 1
    print("")