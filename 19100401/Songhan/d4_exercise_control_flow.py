#使用for...in循环打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
            #print默认是打印一行，然后默认换行，'\t'代表制表符，end=说明打印后跟空格，即下一个打印接着后面输出
        if i==j:
            print () #换行   

#使用while循环打印九九乘法表并用条件判断把偶数行去除掉
i=1
while i<10:
    j=1
    while j<10:
        if i%2==0:
            break
        print(j,'*',i,'=',j*i,sep='',end='\t')
        j+=1
    print()
    i+=1    