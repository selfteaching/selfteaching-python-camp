# print('hello', 'world',18, sep='-')
# print('hello,world',end='*')
# print('hello,world',end='')
# print('hello,world',end='')



# for i in range(1,10):
#     for j in range(1,10):
#         print(f'{i} * {j} = {i*j:2d}',end='    ')
#     print('')



# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j:2d}',end='    ')
    print()


# 偶数行去掉的九九乘法表
i = 1
while i < 10:
    j = 1
    while j <= i:
        if i % 2 == 0:
            print()
            break
        print(f'{i}*{j}={i*j:2d}',end='    ')
        j += 1
    i += 1
       