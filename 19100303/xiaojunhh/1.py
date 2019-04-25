x1=int(input("请输入数字一："))
op=(input("请输入运算符号：+，-，*，/"))
x2=int(input("请输入数字二：") )
if op=="+":
    print(x1+x2)
elif op=="-":
    print(x1-x2)
elif op=="*":
    print(x1*x2)
elif op=="/":
    print(x1/x2)
else:
    print("不支持运算")