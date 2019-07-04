#for 循环打印乘法表
for i in range(1,10):
    for j in range(1,i+1):
        if(i==j):
            print(i,"*",j,"=",i*j)
        else:
            print(i,"*",j,"=",i*j,end="   ")
print()
print()
print()


x=1
y=1
while(x<10):
    while(y<10):
        if(x==y):
            print(x,"*",y,"=",x*y)
            y=1
            x+=2
        else:
            print(x,"*",y,"=",x*y,end="    ")
            y+=1
        break