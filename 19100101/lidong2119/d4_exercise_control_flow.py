a=9
for i in range(1,1+a):
    for j in range(1,1+i):
        print(i,'x',j,'=',i*j,end='\t')
else:
    print(' ')


#使用while函数打印乘法表并用if函数把偶数去掉
i = 1
j = 1
while(i<10):
    while(i%2 != 0):
        while(j <=i):
            print(i,'x',j,'=',i*j,'\t',end='')
            j=j+1
        else:
            print(end='\n')
        break
    i=i+1
    j=1