#day4 
#way 1 使用for...in循环打印出九九乘法表
for i in range(1,10):
    for j in range(1,i + 1):
        print(f'{i} * {j} = ',i*j,end = '\t')
    print()

#way 2 使用while语句+if语句打印出奇数行九九乘法表
m = 1
while m < 10:
    if m % 2 == 0:
        m +=1
    n = 1
    while n < m + 1:
        print(f'{m} * {n} = ', m*n,end = '\t')
        n += 1
    print()
    m += 1
    
   