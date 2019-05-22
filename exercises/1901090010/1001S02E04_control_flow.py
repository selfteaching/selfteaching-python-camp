print('------------for循环九九乘法表------------')
for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, '×', i, '=', i * j, end='\t', sep='')
    print()

print('------------while循环九九乘法表-----------')
i = 1
while i <= 9:
    j = 1
    while j <= i :
        if i %2 ==0: 
            pass
        else:
            print("%d*%d=%-2d " % (j,i,i*j), end = "")
        j += 1
    print()
    i += 1

