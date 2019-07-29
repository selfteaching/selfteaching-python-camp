# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
#跳过偶数行九九乘法表
i = 1
while i < 10:
    if i % 2 == 0:
        print()
    else:
        for j in range(1,i+1):
            print('{}x{}={}\t'.format(j, i, i*j), end='')
    i+=1