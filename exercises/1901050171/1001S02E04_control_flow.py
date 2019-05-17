#使用for循环打印九九乘法表
for i in range(1,10):
    for j in range(1,10):
        if i<=9:
            print(f"{j}*{i}={i*j}",end="\t")
    print("")




#使用while循环打印奇数行乘法表
x=1
while x<=9:
    print()
    y=1
    if x%2==0:
        x+=1
    while y<=x:
        print("{}*{}={:<2}".format(x,y,x*y),end="")
        y+=1
    x+=1