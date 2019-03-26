for i in range(1,10):
    for j in range(1, i+1):
        sum = i * j
        print(str(i) + "*" + str(j) + "=" + str(sum), end='\t')
    print()


print('-----while循环-----')

x = 1
while x <= 9:
    y = 1
    while y <= x:
        mul = x * y
        print(str(x) + "*" + str(y) + "=" + str(mul), end='\t')
        y = y + 1
    print()
    x = x + 2



