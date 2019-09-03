#按照格式输出9*9乘法表：

for i in range(1,10):
    for j in range(1,10):
        if i>=j:  #当i大于等于j的时候才输出
            print(i,"*",j,"=",i*j,'\t',end='')
    print('')
print('')
m=1
while (m<10):
    n=1
    while (n<10):
        if m>=n:
            print(m,"*",n,"=",m*n,'\t',end='')
        n+=1
    print('')
    m+=2
