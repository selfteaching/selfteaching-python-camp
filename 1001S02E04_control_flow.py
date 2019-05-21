#使用for循环打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end='\t')
    print()
    
#使用while循环打印奇数行乘法表
i=1
while i<=9:
    if i%2!=0:
        j=1
            print(f'{i}*{j}={i*j}',end='\t')
            j=j+1
    print()
    i=i+1
    
   
