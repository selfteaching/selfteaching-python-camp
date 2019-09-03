print('九九乘法表\n')
for x in range(1, 10):
    for y in range(1, x+1):
        print('{}x{}={}'.format(x,y,x*y),end = ' ')
    print()

print('\n\n去偶数行的九九乘法表\n')
x = 1
while x <= 9:
    y = 1
    while y <= x:
        if x % 2 == 0:
            break
        print('{}x{}={}'.format(x,y,x*y),end = ' ')
        y += 1
    x += 1
    print()
