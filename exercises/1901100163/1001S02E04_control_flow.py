#用for...in打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,'\t',end=' ')
        if i == j:
           print()

#用while打印乘法表，并去除偶数项
x=1
while x<10:
    y=1
    while y<=x:
        if x%2!=0:
            print(x,'x',y,'=',x*y,'\t',end='')
        y+=1
    while x%2!=0:
        print('')
        break
    x+=1
