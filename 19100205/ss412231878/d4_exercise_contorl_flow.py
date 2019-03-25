#这是一个99乘法表，用for in和while做的

for x in range(1,10):#规定x的范围
    for y in range(1,x+1):#规定每个循环里y等于1到x+1
        print("%s*%s=%s"%(x,y,x*y),end='  ')#定义输出格式和内容，并在每一个输出后加空格隔开
    print()#让每一个循环后自动换行


for x in range(1,10,2):#同上一个，不同的是rangge里规定了1到9，但是以2为间隔
    for y in range(1,x+1):
        print("%s*%s=%s"%(x,y,x*y),end='  ')
    print()

    
a=-1#定义a的初始值
b=0#定义b的初始值
while(a<9):#当a小于9时进行循环
    a+=2#满足上一条的a值加2
    while(b<9):#当b小于9时进行循环
        b+=1#满足上一条时b值加1
        print('%s*%s=%s'%(a,b,a*b),end='\t')#定义输出和内容，并限制自动转行
        if a==b:#当a=b时
            b=0#b值重新变为0
            print()#并转行
            break#结束循环

#利用求余函数
n=1
m=1
while (n <= 9):
    if n%2 != 0:
        while (m<=n):
            print('%s*%s=%s'%(m,n,m*n),end=' ')
            m+=1
        print()
        n+=1#若直接n+=2，就不需要后面的else了
        m=1
    else:
        n+=1