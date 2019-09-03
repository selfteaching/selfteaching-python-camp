x=int(input('请输入第一个数：'))
y=int(input('请输入第二个数：'))

print('加法请选1')
print('减法请选2')
print('乘法请选3')
print('除法请选4')

def 加(x,y):
    print(x,'+',y,'=')
    return x+y

def 减(x,y):
    print(x,'-',y,'=')
    return x-y

def 乘(x,y):
    print(x,'*',y,'=')
    return x*y

def 除(x,y):
    print(x,'/',y,'=')
    return x/y

a=int(input('请选择：'))

if a==1:
    print(加(x,y))
if a==2:
    print(减(x,y))
if a==3:
    print(乘(x,y))
if a==4:
    print(除(x,y))