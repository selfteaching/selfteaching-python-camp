# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{i}*{j}={i*j}',end='\t')
    print()

# 无偶数行的九九乘法表
while True:
    for a in range(1, 10):
        if a % 2 == 0:
            continue
        for b in range(1, a+1):
            print(f'{a}*{b}={a*b}', end='\t')
        print()
    else:
        break

# 只用while和if打印无偶数行的九九乘法表
i = 1
while i <=9:
    if i % 2 != 0:
        j = 1
        while j <= i:
            print(f'{i}*{j}={i*j}', end='\t')
            j += 1
        print()
    i += 1
