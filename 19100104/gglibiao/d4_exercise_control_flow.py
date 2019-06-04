#用for...in循环打印九九乘法表
for i in range(1,10):
    for j in range(1,10):
        print(i, '*', j, '=', i*j, end='\t')
        if i == j:
            print('')
            break 
            
#用while循环打印九九乘法表并去除偶数行
i=0
j=0
while(i<9):
    i+=1
    if i%2==0:
        i+=1
    while (j<9):
        j+=1
        print(i, "*", j, '=', i*j, end='\t')
        if  i==j:
            j=0
            print('')
            break