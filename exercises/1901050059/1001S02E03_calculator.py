def add(x, y):
    print("x is {} and y is {}".format(x,y))
    print(x + y)

def sub(x,y):
    print("x is {} and y is {}".format(x,y))
    print(x - y)

def mul(x,y):
    print("x is {} and y is {}".format(x,y))
    print(x * y)

def div(x,y):
    print("x is {} and y is {}".format(x,y))
    print(x / y)

x = int(input("输入第一个数字: "))
y = int(input("输入第二个数字: "))
a = input("选择 + - * /: ")
if a == '+':
    add(x,y)
elif a == '-':
    sub(x,y)
elif a == '*':
    mul(x,y)
elif a == '/':
    div(x,y)
    
