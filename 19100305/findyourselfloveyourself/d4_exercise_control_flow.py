#左下三角格式输出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print (" ")
    x = 1

while x <= 9:
    y = 1
    while y <= x:
        if x % 2 == 1:
            print('%d*%d=%d\t' % (x, y, x*y), end='')
        y += 1
    if x % 2 == 0:
        print()
    x += 1