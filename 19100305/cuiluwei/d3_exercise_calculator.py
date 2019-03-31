a=float(input("请输入："))
b=input("请输入运算符:")
c=float(input("请输入:"))
if b=="+":
    print(a+c)
elif b=="-":
    print(a-c)
elif b=="*":
    print(a*c)
elif b=="/":
    print(a/c)
else:
    print("输入错误，请重新输入")