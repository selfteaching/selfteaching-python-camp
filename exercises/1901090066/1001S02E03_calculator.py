a = float(input("请输入第一个数字: "))
b = float(input("请选择运算符:1是+，2是-，3是*，4是／"))
c = float(input("请输入第二个数字: "))
def add(x,y):
    return x+y
def sub(x,y):
    return x-y   
def mul(x,y):
    return x*y
def div(x,y):
    return x/y   
if b == 1:
    print("a - b = ",add(a,c))
elif b == 2:
    print("a - b = ",sub(a,c))
elif b == 3:
    print("a * b = ",mul(a,c))
elif b == 4:
    print("a / b = ",div(a,c))
