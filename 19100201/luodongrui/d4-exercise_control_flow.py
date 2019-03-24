# 九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        d = i * j
        print('%d*%d=%-2d'%(i,j,d),end = ' ' )
    print()

# 除去偶数列的九九乘法表

i = 1
while i <= 9:
    j = 1
    while j <= i:
        if i%2==1:
            print('%d X %d = %d' % (j,i,i*j),end = '  ') 
        j += 1
    print('')
    i += 1