# 九九乘法表
# author:Sandra.Z
print('九九乘法表')
for x in range(1, 10):
    print(x, end= '\t')
    for y in range(1, x+1):
        print(x, '*', y, '=', x*y, end='\t')
    print()

print('跳过偶数行的九九乘法表')
x = 1
while x < 10:
    if x % 2 == 0:
        print()
    else:
        for y in range(1, x+1):
            print(x, '*', y, '=', x*y, end='\t')
    x += 1