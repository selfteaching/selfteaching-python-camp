
#while循环九九乘法表

n = 1
while n<10:
    for i in range(1,n+1):
        print(n,'*',i,'=',i*n, sep='',end='\t')
    print()
    n=n+1

# for九九乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        if i % 2 == 0:
            print(i, '×', j, '=', i * j, end='\t', sep='')
    print()

#while循环去偶数行
i = 1
while i < 10:
    j = 1
    while j < i + 1:
        if i%2 == 0:
            break
        print(i, '×', j, '=', j * i, sep='', end='\t')
        j += 1
    print()
    i += 1 
