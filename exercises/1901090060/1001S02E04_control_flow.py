for m in range(1,10):
    for n in range(1,10):
        print('%s*%s=%s'%(m,n,m*n),end='')
        if  n>m:
            break
    print()



#coding=utf-8
print(str('去掉偶数行的九九乘法表'))
i = 1
while i<=9:
    if i % 2 ==0:
        print()
    else:
        for j in range(1,i+1):
            print(i,'*',j,'=',i*j,end='\t')
    i += 1
    