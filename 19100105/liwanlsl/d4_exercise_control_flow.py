# 乘法口诀
for x in range(1,10):  # x的范围1=<x<10 
    for y in range(1,x+1):   # y的范围1=<y<x+1 
        print(x,'x',y,'=' ,y*x,end='  ')  # y<x+1为ture时，输出x*y=乘积，并两个空格
    print(end='\n')   # y<x+1为flase时，换行

# 增加空行
print('\n')

x=1   # 初设x=1
while x<10:  # x的范围
    y=1   # 在上述条件下，初设y=1
    if(x%2==1):   # 若x/2余数为1为ture时
        while y<x+1:  # y的范围 y<x+1
            print( x,"x", y,"=" ,x*y,end="  ")  # y<x+1为ture时，输出x*y=乘积，并两个空格
            y=y+1  # 且返回新y=y+1
        print (end="\n")  # y<x+1为flase时，换行
        x=x+1  # 且返回新x=x+1
    else:
        x=x+1  # 若x/2余数为1为flase时，返回新x=x+1