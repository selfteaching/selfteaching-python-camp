for i in range(1,10):#定义1-9
    for j in range(1,i+1):#按照1—i顺序
        print(i,"*",j,"=",i*j," ",end='\t')#多次调试，必须要加上end='\t'
    print(" ")#加上空格
#以上是使用for...in循环打印九九乘法表

print("")
#下面开始使用while循环打印九九乘法表并使用条件判断把偶数行去
i=1
while i<=9:
    if i%2==0:
        i+=1
    j=1
    while j<=i:
        print(i,"*",j,"=",i*j,end='\t')
        j+=1
    i+=1
    print(" ")    
