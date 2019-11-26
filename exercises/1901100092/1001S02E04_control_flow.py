print('打印九九乘法表')
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()

print('打印去年偶数行的九九乘法表')
i=1
while i<10:
    if i%2==0:
        print()
    else:
        for j in range(1,i+1):
            print(i,'*',j,'=',i*j,end='\t')
    i+=1

print('打印去掉偶数行的九九乘法表')
for i in range(1,10):
    for j in range(1,i+1):
        if i%2==0:
            print()
            break
        print(i,'*',j,'=',i*j,end='\t')