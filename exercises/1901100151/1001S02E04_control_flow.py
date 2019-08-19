# day 4 work.

# 完整乘法表
for i in range(1, 10):
    # print(i)
    for j in range(1,i+1):
        # print (j)
        print(i, "*", j, "=", i * j, end= '\t')
    print()

# 偶数乘法表
for i in range(1,10):
    if i % 2 == 1:
        print()
    else:
        for j in range(1,i + 1):
            print(i, "*", j, "=", i * j, end= "\t")
print()

# 奇数乘法表
for i in range(1,10):
    if i % 2 == 0:
        print()
    else:
        for j in range(1,i + 1):
            print(i, "*", j, "=", i * j, end= "\t")
print()

# 奇数乘法表
print()
i = 1
while i < 10:
        if i % 2 == 0:
            print()
        else:
            for j in range(1,i + 1):
                print(i, "*", j, "=", i * j, end= "\t")
        i += 1