print("使⽤用 for...in 循环打印九九乘法表！")
for i in range(1,10,1):
    for j in range(1,i+1,1):
        if(j < i):
            print(str(i) + "*" + str(j) + "=" + str(j*i) , end = "\t")
        else:
            print(str(i) + "*" + str(i) + "=" + str(j*i) , end = "\n") 

print("使⽤用 while 循环打印九九乘法表并⽤用条件判断把偶数⾏行行去除掉！")
i = 1
j = 1

while i <= 9:
        if(i % 2 == 0):
            j = 1
            i = i+1
        else :
            while(j <= i):
                    print(str(i) + "*" + str(j) + "=" + str(j*i) , end = "\t")
                    j = j+1
            else:
                    j = 1
                    i = i+1
                    print(end = "\n")
                    continue