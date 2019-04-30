a=float(input('请输入数值1')) # float()支持小数运算，如果用int()函数的话就只支持输入整数了，input()接收键盘输入
b=input('请输入运算符号')
c=float(input('请输入数值2'))
if b=="+":
    print(a+c)
elif b=="-":
    print(a-c)
elif b=="*":
    print(a*c)
elif b=="/":
    print(a/c)
elif b=="**":
    print(a**c)
elif b=="%":
    print(a%c)