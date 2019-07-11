# ֵ使用for...in 循环打印九九乘法表，输出：
for i in range(1,10):
    for j in range(1, i + 1):
        print( i,'*',j ,'=', i * j, end='\t')
    print()

# 使用while循环打印九九乘法表并用条件判断把偶数行去掉
for i in range(1,10):
    if (i % 2) == 0:
        continue
    for j in range(1, i + 1):
        print ( i,'*',j ,'=', i * j, end='\t')
    print()
    