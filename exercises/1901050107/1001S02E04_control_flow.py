
#使⽤用for...in循环打印九九乘法表，输出
for i in range(1,10):
    for k in range(1,i+1):
        print(str(i)+"*"+str(k)+"="+str(i*k),end = "\t")
    print()        
print()
#使⽤用while循环打印九九乘法表并⽤用条件判断把偶数⾏行行去除掉，输出:
i = 1
while i <= 9:
    if i % 2 != 0:
        for k in range(1,i+1):
            print(str(i)+"*"+str(k)+"="+str(i*k),end = "\t")
        print() 
    i += 1  