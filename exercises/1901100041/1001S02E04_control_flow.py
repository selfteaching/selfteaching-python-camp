
print('九九乘法表')
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(i, j, i*j), end='')
    print()


print('\n跳过偶数行的九九乘法表')
i = 1
while i < 10:
    if i % 2 ==0:
        print()
    else:
        for j in range(1, 10):
            print('{}x{}={}\t'.format(i, j, i*j), end='')
    i += 1
        

