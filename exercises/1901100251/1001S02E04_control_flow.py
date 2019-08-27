#使⽤for...in循环打印九九乘法表
for a in range (1,10):
    for b in range (1,10):
        print (a,"x",b, "=",a*b,"\t", end= "")
        if a == b:
            print ("")
            break






#使用while循环打印九九乘法表并⽤条件判断把偶数行去除掉
for a in range (1,10):
    for b in range (1,10):
        while a % 2 == 0:
            break
        else:
            print(a,"x",b,"=",a*b,"\t", end="")
            if a == b:
                print ("")
                break