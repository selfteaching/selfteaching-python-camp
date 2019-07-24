print("使用for...in循环打印乘法表")
for i in range (1,10):     #对数组中的每个元素都执行相同的操作
    for j in range(1,10):  
        print(i,"x",j,"=",i*j,end="\t") #以制表符结尾
        if i==j:
            print("")
            break


print("用while循环打印乘法表")
i=0                    #i从0开始
j=0                    
while i<9:             #只要i<9，就接着运行这个循环
    i+=1               #将i的值加1赋给j
    while j<9:         
        j+=1           
        print(i,"x",j,"=",i*j,end="\t")
        if i==j:       
            j=0        #将j的值置为0
            print("")  
            break      #退出循环


print("打印出奇数行乘法表")
i=0
j=0
while i<9:
    i+=1
    if i % 2 != 0:   #如果i除以2的余数为0，即i为偶数
        while j<9:
            j+=1
            print(i,"x",j,"=",i*j,end="\t")
            if i==j:
                j=0
                print("")
                break

print("打印出奇数行乘法表，有空白行") #测试多个条件
i=0
j=0
while i<9:
    i+=1
    while j<9:
          j+=1
          if i % 2 != 0:
              print(i,"x",j,"=",i*j,end="\t")
          if i==j:  #不管前面测试结果如何都将执行这些代码
             j=0
             print("")
             break          