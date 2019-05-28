# for i in range(1, 10):
#     for j in range(1, i):
#         print('{}x{}={}'.format(i, j, i*j))

for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}'.format(i, j, i*j), end=' ')
    print()


# for i in range(1,10):
#     for j in range(1,i+1):
#         if i%2==0:
#             continue
#         print('{}x{}={}'.format(i, j, i*j), end=' ')
#     print()
print('-----------------------------------------------------------------------')
x = 1
while (x < 10):
    y = 1
    while(y <= x):
        if x % 2 == 1:
            print('{}x{}={}'.format(x, y, x * y), end=' ')
        y = y+ 1
    x = x + 1
    if x % 2 == 1:
        print()
print('')