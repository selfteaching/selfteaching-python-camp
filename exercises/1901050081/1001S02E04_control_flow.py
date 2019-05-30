print('用if in 循环制作九九乘法表：')
for i in range(1,10):
    for j in range(1,i+1):
        d=i*j
        print('{}*{}={}'.format(i,j,d),end='\t')
    print()
print('\n')
print('用while循环制作九九乘法表，并用条件判断把偶数行去掉：')
i=1
while i<10:
    j=1
    while j<=i:
        print('{}*{}={}'.format(i,j,i*j),end='\t')
        j+=1
    print()
    i+=2