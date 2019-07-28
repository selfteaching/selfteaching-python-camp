# 为实现计算器的编程，需要先制定一个稳定的运行环境。


# 计算器的第一步流程是输入参数。
operator=input("请输入需要应用的四则运算方式：+，-，*，/。")
number1=input("请输入第一个计算数字。")
number2=input("请输入第二个计算数字。")
a=int(number1)
b=int(number2)

# 自动反馈输入数据以便验证是否正确。
print("operator:",operator,type(operator))
print("number1:",number1,type(number1),type(a))
print("number2:",number2,type(number2),type(b))

# 计算器的第二步流程是运算和输出。
if operator == "+":
    print(a,"+",b,"=",a+b)
elif operator == "-":
    print(a,"-",b,"=",a-b)
elif operator == "*":
    print(a,"*",b,"=",a*b)
elif operator == "/":
    print(a,"/",b,"=",a/b)
else:
    print("输入有误。")

#计算器编写完成。