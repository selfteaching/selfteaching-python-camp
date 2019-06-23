#使用 for...in 循环打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        result=i*j
        print(f'{i}*{j}={result}',end=' ')
    print("")
print('\n')

#使用 while 循环打印九九乘法表并用条件判断把偶数行去掉
i=1
while i <10:
    j=1
    while i%2 !=0:
        while j <=i:
            re=i*j
            print(f'{i}*{j}={re}',end=' ')
            j+=1
        else:
            print('')
        break
    i+=1   