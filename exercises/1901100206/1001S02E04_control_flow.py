#第一版作业：自己做出
for x in range(1, 10):
    for y in range(1, 10):
        if x == y:
            print("{} * {} = {}".format(x, y, x*y))
        elif x > y:
            print("{} * {} = {}".format(x, y, x*y), end='\t')
#改进版：搜索得出
for x in range(1, 10):
    for y in range(1, x+1):
        print("{} * {} = {}\t".format(x, y, x*y), end='')
    print()

#有点卡壳，通过Google搜索然后改进。
x = 1
while x <= 9:
    y = 1
    while y <= x:
        if x % 2 != 0:
            print('{}x{}={}\t'.format(x, y, x*y), end='')
        y = y + 1
    x = x + 1
    print("")