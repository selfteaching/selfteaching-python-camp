def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("选择运算符号：+，-，*，/")
c=input("")
a=int(input("输入数字："))
b=int(input("输入数字："))
if c=="+":
    print(add(a,b))
elif c=="-":
    print(subtract(a,b))
elif c=="*":
    print(multiply(a,b))
elif c=="/":
    print(divide(a,b))
else:
    print("错误")            