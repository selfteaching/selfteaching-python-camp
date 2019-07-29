# 乘法表
for i in range(1,10): #变量i的范围是1到10
    for k in range(1,i+1): #变量k的范围是1到i+1
        print ("%d*%d=%2d" % (i,k,i*k),end="") 
    print()

#整数*整数=2位整数 



print('\n\n去偶数行的九九乘法表\n')
x = 1
while x <= 9:
    y = 1
    while y <= x:
        if x % 2 == 0:            #x的余数是0，也就是偶数
            break
        print('{}x{}={}'.format(x,y,x*y),end = ' ')
        y += 1             #y+1=y
    x += 1                 #x+1=x
    print()