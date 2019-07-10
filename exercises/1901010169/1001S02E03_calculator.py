import operator
x = float(input("请输入第一个数字："))
z = input("+,-,*,/:""   ")
#减法
if z == "-":
    y = float(input("请输入第二个数字: "))
    print(x, "-" ,y, "=",operator.sub(x,y)) 
elif z == "+":
#加法
    y = float(input("请输入第二个数字：")) 
    print(x, "+" ,y, "=",operator.add(x,y))
elif z == "*":
#乘法
    y = float(input("请输入第二个数字：")) 
    print(x, "*" ,y, "=",operator.mul(x,y))
elif z == "/":
#除法
    y = float(input("请输入第二个数字：")) 
    print(x, "÷" ,y, "=",operator.truediv(x,y))25