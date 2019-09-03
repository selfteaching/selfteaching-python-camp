# 1、使⽤for...in循环打印九九乘法表
for m in range(1,10):
    for n in range(1,m+1):
        print(m,'×',n,'=',m*n,end='\t')
    print('\n')

# 2、使⽤ while 循环打印九九乘法表并⽤条件判断把偶数⾏去除掉
m = 1
while m <= 9:
    n = 1
    if m % 2 == 1:# 奇数odd
        while n<=m:
            print(m,'×',n,'=',m*n,end='\t')
            n += 1
        print('\n')
    else:
        pass
    m += 1



# 偶数even：num % 2 == 0；奇数odd：num % 2 == 1；
#for num in range(1, 10):
#    if num % 2 == 0:
#        print("Found an even number", num)
#    continue
#    print("Found a number", num)
