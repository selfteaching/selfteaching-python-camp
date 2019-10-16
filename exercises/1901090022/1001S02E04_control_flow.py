# coding: utf-8

print("===== 使⽤ for...in 循环打印九九乘法表 =====")
for row in range(1, 10):
    for col in range(1, 10):
        print("{}*{}={} ".format(row, col, row*col), end="  ")
        if col == row:
            print("")
            break
print("===== 使⽤ while 循环打印九九乘法表并⽤条件判断把偶数⾏去除掉 =====")

row = 1
col = 1
while row < 10:
    if row%2 == 0:
        row += 1
        continue
    while col < 10:
        print("{}*{}={} ".format(row, col, row*col), end="  ")
        if col == row:
            print("")
            col = 1
            break
        col += 1
    row += 1