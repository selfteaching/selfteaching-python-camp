print("使用for循环打印九九乘法表")
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j,i,i*j),end='')

    print()


print()

print("使用while循环打印九九乘法表，去掉偶数部分")
x=1
while x <= 9: 
    print()
    y=1
    if x%2==0:
        x+=1
    while y <= x:
        print("{}x{}={:<2}".format(x,y,x*y),end=" ")
        y+=1
    x+=1
    
    
    