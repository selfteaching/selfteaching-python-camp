#使用for...in循环打印九九乘法表
print('for...in循环打印九九乘法表')
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t',sep='')
    print()

#使用while循环打印九九乘法表
print('while循环打印九九乘法表')
i=1
while i<10:
    j=1
    while j<i+1:
        if i%2==0:
            break
        print(i,'*',j,'=',i*j,end='\t',sep='')
        j+=1
    print()
    i+=1