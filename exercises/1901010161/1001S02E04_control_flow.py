print('九九乘法表')
for x in range(1, 10):
    for y in range(1, x+1):
        print("{}×{}={}\t".format(x, y, x*y), end='  ')
        if x == y:
            print("")
            break

# 打印奇数表
print('九九乘法表-奇数表')
for a in range(1, 10):
    for b in range(1, a+1):
        while a % 2 != 0:
            print("{}×{}={}\t".format(a, b, a*b), end='  ')
            if a == b:
                print("")
            break
        else:
            pass
