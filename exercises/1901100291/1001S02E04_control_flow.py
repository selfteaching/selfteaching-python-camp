#使用for...in 循环打印九九乘法表
print('使用for...in 循环打印九九乘法表')


for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, '*', i, '=', i * j, end="\t")
    print()

print()
#使用 while 循环打印九九乘法表并用条件判断把偶数去除掉
print('使用 while 循环打印九九乘法表并用条件判断把偶数去除掉')
i=1
while i < 10 :
    j=1
    while j <= i :
        print(i,'*',j,'=',i*j,end='\t')
        j=j+1
    print()
    i=i+2

