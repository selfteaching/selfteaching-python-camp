print('使用 for...in 循环打印九九乘法表，输出：')
print()
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%-2d'%(i,j,i*j),end='  ')
    print()

print()

print('使用 while 循环打印九九乘法表，并用条件判断把偶数行去掉，输出：')
print()

i=1
while i<=9:
    if i%2!=0:
        j=1
        while j<=i:
            print('%d*%d=%-2d'%(i,j,i*j),end='  ')
            j+=1
        print()
    i+=1
   



