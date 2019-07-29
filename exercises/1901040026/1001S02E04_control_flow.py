print("《九九乘法表》")
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, 'x', i, '=', i*j, end='\t')
        if i == j:
            print()


print("\n《九九乘法表-奇数行》")
for a in range(1, 10):
    for b in range(1, a+1):
        while a % 2 != 0:
            print(b, 'x', a, '=', a*b, end='\t')
            if a == b:
                print()
            break
