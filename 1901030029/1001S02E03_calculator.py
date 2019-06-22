#创建一个支持加减乘除的计算机代码
def calculation():
    number1=float(input("请输入第一个数字："))
    operator=input("请输入以下运算方式：+-*/")
    if  operator=="+":
        number2=float(input("请输入第二个数字："))
        input("答案是：",number1+number2)
    elif operator=="-":
        number2=float(input("请输入第二个数字："))
        print("答案是：",number1-number2)
    elif operator=="*":
        number2=float(input("请输入第二个数字："))
        print("答案是：",number1*number2)
    elif operator=="/":
        number2=float(input("请输入第二个数字："))
        print("答案是",number1/number2)
    else:
        print("您输入的算术方式错误。")

calculation()

