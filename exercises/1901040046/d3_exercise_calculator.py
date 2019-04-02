#创建一个加减乘除计算器
def calculation():
    number1 = float(input("请输入第一个数字："))
    operator = input("请从以下选择一种算数方式：“+-*/”：")
   
    if operator == "+":
        number2 = float(input("请输入第二个数字："))
        print("答案是：",number1+number2)
    elif operator == "-":
        number2 = float(input("请输入第二个数字："))
        print("答案是：",number1-number2)
    elif operator == "*":
        number2 = float(input("请输入第二个数字："))
        print("答案是：",number1*number2)
    elif operator == "/":
        number2 = float(input("请输入第二个数字："))
        print("答案是：",number1/number2)
    else:
        print("输入计算方式错误")

calculation()      
