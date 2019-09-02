print("极简计算器：加减乘除考考它")

x=float(input("请输入第一个数字："))
choice=input("请输入运算符号(仅限“+”，“-”，“*”，”/“)：")
y=float(input("请输入第二个数字："))

if choice=="+":
    print(x,"+",y,"=",x+y)
elif choice=="-":
    print(x,"-",y,"=",x-y)
elif choice=="*":
    print(x,"*",y,"=",x*y)
elif choice=="/":
    print(x,"/",y,"=",x/y)
else:
    print("无效输入！") 