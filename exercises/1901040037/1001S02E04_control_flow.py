print('---for 循环九九乘法表-----')
for i in range(1,10):
    for j in range(1, i+1):
        print(i,'x',j,'=',i*j,end='\t')
    print()

print('---使用while 循环打印九九乘法表并且去掉偶数行---')
for i in range(1,10):
    while i%2 != 0:
        for j in range(1, i+1):
            print(i,'x',j,'=',i*j,end='\t')
        i = i+1
    print()

