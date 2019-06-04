#for...in打印九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        a=i*j
        print(f'{i}*{j}={a}',end=' ')     #花括号是什么意思？
    print("")                             #为什么加这个就变成梯形了？print("")位置不同，结果不同
 
#使用while打印九九乘法表，并用条件判断把偶数去掉


i=1                      #为什么要有这句话，作用是啥？
while i<10:
    j=1
    while i%2!=0:
        while j<=i:
            re=i*j
            print(f'{i}*{j}={re}',end=' ')
            j+=1              #从这里开始不明白
        else:
            print('')
        break
    i+=1

            
        