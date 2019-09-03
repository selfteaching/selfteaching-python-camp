#左下三角格式输出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print (" ")
    
    print('\n\n去偶数行的九九乘法表\n')
i = 1
while i <= 9:
    j = 1
    while j <=i:
        if i % 2 ==0:
            break
        print('{}x{}={}'.format(i,j,i*j),end = ' ')
        j += 1
    i += 1
    print()
