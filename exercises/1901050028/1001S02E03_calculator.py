num1 = float(input("请输入一个数字："))
op = input("请输入运算方式：")
num2 = float(input("请输入另一个数字："))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("无效运算")
input("Press <enter>")
