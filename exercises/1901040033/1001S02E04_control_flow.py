print('九九乘法表')
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(i,j,i*j),end='  ')
    print('')

############################

print(' ')
print('九九乘法表去偶数')
i=1
while i<=9:
    j=1
    while j<=i:
        if i % 2 == 0:
            break
        print('{}*{}={}'.format(i,j,i*j),end='  ')
        j += 1
    i += 1
    print()


     
    