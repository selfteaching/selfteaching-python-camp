# 使用for...in循环打印九九乘法表
print('九九乘法表')
for x in range(1, 10):   
    for y in range(1, x + 1):
        print('{0:d}x{1:d}={2}\t'.format(x, y, x * y), end='')
    print('')



#使用while循环打印九九乘法表并用条件判断把偶数行去除掉
print('九九乘法表 奇数行')
x=1
while x<=9:
    if x % 2 == 0:
        x += 1
        continue
    y = 1
    while y<=x:
        print('{0:d}x{1:d}={2}\t'.format(x, y, x * y), end='')
        y=y+1
    print('')
    x+=1
   

    