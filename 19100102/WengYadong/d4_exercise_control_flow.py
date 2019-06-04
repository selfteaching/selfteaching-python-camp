# 使用Python的for...in循环打印九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j,i, i*j), end='')
    print()

print("--------------------------------------------------------------------------------------------------")

#使用Python的while循环打印九九乘法表并用条件判断把偶数行去掉
i=1
while i<10:
    j=1
    while j<=i:
        if i%2==0:
            j+=1
            continue
        print("%d*%d=%2d "%(j,i,i*j),end="")
        j+=1
        
    i+=1
    print()

print("--------------------------------------------------------------------------------------------------")

#用Python的while循环打印九九乘法表并用条件判断把偶数行去掉（改进版）
i = 1
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    j = 1
    while j < i + 1:
        print(i,"*",j,"=",i*j,"",end="")
        j += 1
    print("",end="\n")
    i += 1