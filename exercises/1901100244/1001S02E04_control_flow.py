# -*- coding: UTF-8 -*-

# Filename : 1001S02E04_control_flow.py
# author by : @shen-huang

# 打印两种九九乘法表

# 任务原始要求

for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print("{0}*{1}={2}".format(i, j, i*j), end='   ')
    print()
print()

for i in range(1, 10):
    while i % 2 != 0:
        for j in range(1, 10):
            if j <= i:
                print("{0}*{1}={2}".format(i, j, i*j), end='   ')
        print()
        break
print()

print("――――――――――――――――――――――――――――――――――――――――")
print()

# 任务其他尝试

# 使用符合标准的乘号（×）

# 修改为常见的九九表呈现方式

for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print("{0}×{1}={2}".format(j, i, i*j), end='\t')
    print()
print()

# 修改为另一种方向的九九表呈现方式

for i in range(1, 10):
    for j in range(1, 10):
        if i > j:
            print("     ", end='\t')
        else:
            print("{0}×{1}={2}".format(i, j, i*j), end='\t')
    print()
print()

# 考虑该表可能的实际用途，去掉了两数大小判断

for i in range(1, 10):
    while i % 2 != 0:
        for j in range(1, 10):
            print("{0}×{1}={2}".format(j, i, i*j), end='\t')
        print()
        break
print()

# 不同的循环方式，省去了两数大小判断

for i in range(1, 10):
    for j in range(1, i+1):
        print("{0}×{1}={2}".format(j, i, i*j), end='\t')
    print()
print()

for i in range(1, 10):
    while i % 2 != 0:
        for j in range(1, i+1):
            print("{0}×{1}={2}".format(j, i, i*j), end='\t')
        print()
        break
print()

# 不同的循环方式，省去了条件判断（while）

for i in [1, 3, 5, 7, 9]:
    for j in range(1, i+1):
        print("{0}×{1}={2}".format(j, i, i*j), end='\t')
    print()
print()

# 不同的循环方式，使用了 if

for i in range(1, 10):
    if i % 2 != 0:
        for j in range(1, i+1):
            print("{0}×{1}={2}".format(j, i, i*j), end='\t')
        print()
print()

# 不同的循环方式，使用了 continue

for i in range(1, 10):
    if i % 2 == 0:
        continue
        for j in range(1, i+1):
            print("{0}×{1}={2}".format(j, i, i*j), end='\t')
        print()
print()