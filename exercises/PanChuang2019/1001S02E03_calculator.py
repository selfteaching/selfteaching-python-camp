operator = input('请输入运算符(+、-、*、/):')
firstdata = input('请输入第一个数字:')
seconddata = input('请输入第二个数字:')
x = int(firstdata)
y = int(seconddata)
if operator=="+":
    print(x,"+",y,"=",x+y)
elif operator=="-":
    print(x,"-",y,"=",x-y)
elif operator=="*":
    print(x,"*",y,"=",x*y)
elif operator=="/":
    print(x,"/",y,"=",x/y)
else:
    print("运算符输入错误")
