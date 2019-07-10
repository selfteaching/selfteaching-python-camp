print("这是一个计算器")
a = int(input("请输入第一个数字："))
print()
x = str(input("请输入一个运算符 +,-,*,/:"))
print()
b = int(input("请输入第二个数字："))
if x == "+":
    print()
    print(a,"+",b,"=",a+b,)
elif x == "-":
    print()
    print(a,"-",b,"=",a-b,)
elif x == "*":
    print()
    print(a,"*",b,"=",a*b,)
else:
    print()
    print(a,"/",b,"=",a/b,)