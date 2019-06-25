#定义一个计算+-*/的函数，operate代表用户输入的操作符，numA，numB代表用户输入的要计算的数字
def calculate(operate,numA,numB):

    if operate=="+":
        print(numA+numB)
    elif operate=="-":
        print(numA-numB)
    elif operate=="*":
        print(numA*numB)
    elif operate=="/":
        print(numA/numB)
    else:
        print("无效的操作符，请输入+-*/ 任意一个")

operate=input("请输入操作符：")
numA=int(input("请输入你的数字:"))
numB=int(input("请输入你的数字:"))

#调用上面定义的函数calculate
calculate(operate,numA,numB)  