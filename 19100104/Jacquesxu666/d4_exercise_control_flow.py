for i in range(1, 9): # 用for in 打印任务
    for j in range(1, 9):
        print(i, "*", j, "=", i*j, end='\t')
        if j == i:
            print("")
            break
for k in range(1, 9):
    print(9, "*", k, "=", 9*k, end='\t')
print("")
print(9, "*", 9, "=", 81)
        
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
print('')
print(9, "*", 9, "=", 81)



