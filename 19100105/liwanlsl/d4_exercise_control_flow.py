# 乘法口诀
for x in range(1,10):  # x的范围1=<x<10 
    for y in range(1,x+1):   # y的范围1=<y<x+1 
        print(x,'x',y,'=' ,y*x,sep='',end='\t')  # y<x+1为ture时，输出x*y=乘积
    print()   # y<x+1为false时，换行

# 增加空行
print()

for x in range(1,10) :  # x的范围
    if(x%2==1):   # 若x/2余数为1为ture时
        for y in range(1,x+1) :  # y的范围 y<x+1
            print( x,"x", y,"=" ,x*y,sep='',end="\t")  # y<x+1为ture时，输出x*y=乘积
        print ()  # y<x+1为false时，换行
