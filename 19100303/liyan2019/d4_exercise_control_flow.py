# 用python编写九九乘法表 ， i控制行,j控制列
print('------------for in 循环九九乘法表-----------')
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")  # 每个算式所占的位置为7个字节，在Python中不能直接写print("  ")语句表示输出空格，必须添加end关键字，表示结尾以等号右边的内容输出。
    print (" ")  # print("")表示换行

print('------------while循环九九乘法表-----------')
i = 1
while i < 10:
    j = 1
    while j < i + 1:
        print(j, '×', i, '=', i * j, sep='', end='\t')
        j += 1
    print()
    i += 1


print('------------while循环九九乘法表并用条件判断把偶数行去掉-----------')# 尚未实现条件判断（if else），待后续补充
i = 1
while i < 10:
    j = 1
    while j < i + 1:
        print(j, '×', i, '=', i * j, sep='', end='\t')
        j += 1
    print()
    i += 1