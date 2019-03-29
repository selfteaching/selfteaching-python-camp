#打印九九乘法表/用条件判断把偶数行去除

def multiply_for(a):
for x in range(1,a+1):
    for y in range(1,x+1):
        print(x,'*',y,'=',x*y,end='\t')
    print()

def multiply_while(a):
    x=1
    while x<=a:
        y=1
        while y<=x:
            print(x,'*',y,'=',x*y,end='\t')
            y=y+1
        print()
        x=x+2

multiply_for(9)
multiply_while(9)