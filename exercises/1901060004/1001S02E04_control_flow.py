# -*-coding: utf-8-*-
# 九九乘法表口诀
for m in range(1,10):
    for n in range(1,10):
        if m>=n:
            print('%sx%s=%s'%(m,n,m*n),end='  ')
    print()

# 不用if语句 打印 九九乘法表
for m in range(1,10):
    for n in range(1,m+1):
        print('%sx%s=%s'%(m,n,m*n),end='  ')
    print()


for i in range (1,10):
    for j in range(1,10):
        print(j,"x",i,"=",i*j,"\t",end="")
        if i==j:
            print(" ")
            break

# 一句代码打印 九九乘法表
print ('\n'.join(['  '.join(['%sx%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))



# 九九乘法表去偶数行
f = 1
while f <= 9:
    if f % 2 != 0:
        h = 1
        while h < f + 1:
            print(f, "x", h, "=",f*h,sep="", end="\t")
            h += 1
        print()
    f += 1


