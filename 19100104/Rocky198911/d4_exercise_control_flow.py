for i in range(1, 10): # 用for in 打印任务
    for j in range(1, 10):
        print(i, "*", j, "=", i*j, end='\t')
        if j == i:
            print("")
            break

        
a, b = 0, 0  # 用while循环打印任务
while (a < 9):
    a += 1
    if a % 2 == 0:
        a += 1
    while (b < 8):
        b += 1
        print(a, "*", b, "=", a*b, end='\t')
        if a == b:
            b = 0
            print('')
            break



