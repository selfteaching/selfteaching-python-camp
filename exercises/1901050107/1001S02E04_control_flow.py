# 使⽤用for...in循环打印九九乘法表
for i in range(1,10):
    for j in  range(1,i+1):
        print(f'{i}*{j}={i*j}',end = ' ')
    print()   
#使⽤用while循环打印九九乘法表并⽤用条件判断把偶数⾏行行去除掉
i = 1
while i < 10:
    if i % 2 != 0:
        for j in  range(1,i+1):
            print(f'{i}*{j}={i*j}',end = ' ')    
        print()    
    i += 1    