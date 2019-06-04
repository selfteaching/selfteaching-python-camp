#用for...in...语句打印乘法九九表
for i in range(1,10):
    for n in range(1,i+1):
            print("%d * %d"%(i,n),"=",i*n,end="\t")
    print()
print()

#用while语句打印乘法九九表，并去除偶数行

x=1
while int(x)<10:
    if x%2==1:
        y=1
        while int(y)<=int(x):
            print(x,"*",y,"=",x*y,end="\t")
            y=y+1
        print()
    x=x+1
