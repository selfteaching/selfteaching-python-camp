#使⽤ for...in 循环打印九九乘法表
'''for i in range(1,10):
        for j in range(1,i+1):                                #内层循环
                print("{}*{}={}".format(i,j,i*j),end=" ")
        print(" ")
'''

#使用for循环打印九九乘法表并把偶数行去掉
'''for i in range(1,10):
        for j in range(1,i+1):                            
         if i % 2==0:
           break
         print("{}*{}={}".format(i,j,i*j),end=" ")
        print(" ")
'''



#使⽤ while 循环打印九九乘法表并把偶数⾏去除掉
'''i = 1
while i<=9:
    j = 1
    while j<=i and i%2!=0:
        print("{}*{}={:<2}".format(i,j,i * j),end = " ")
        j += 1
    i += 1
    print("")'''

#使用while循环打印乘法表并把偶数行去除掉
i = 1
while i<=9:
    j = 1
    while j<=i:
        if i%2==0:
                break
        print("{}*{}={:<2}".format(i,j,i * j),end = " ")
        j += 1
    i += 1
    print("")
  


