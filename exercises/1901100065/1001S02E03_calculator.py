def add(x,y): # 加法函数
    z = x + y
    print("{} + {} = {}".format(x,y,z))
    return

def sub(x,y): # 减法函数
    z = x - y
    print("{} - {} = {}".format(x,y,z))
    return

def mul(x,y): # 减法函数
    z = x * y
    print("{} * {} = {}".format(x,y,z))
    return

def div(x,y): # 减法函数
    z = x / y
    print("{} / {} = {}".format(x,y,z))
    return

a = input("input first number:")
b = input("input second number:")
a = float(a)
b = float(b)
operater = input("choose the Kind of operator (+ , - , * , / )")

if operater == "+":
    add(a,b)
elif operater == "-":
    sub(a,b)
elif operater == "*":
    mul(a,b)
elif operater == "/":
    div(a,b)
else:
    print("the input is wrong, please try again")

