###九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%d\t" % (i, j, i*j),end="")
    print()


###奇数行
i = 1
while i <= 9:
    if i % 2 != 0:
        j = 1
        while j < i + 1:
            print(i, "*", j, '=', i*j, sep='', end=' ')
            j += 1
        print()
    i += 1
   
        