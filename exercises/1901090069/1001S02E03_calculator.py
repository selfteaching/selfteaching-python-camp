#这是一个简单的计算器
i = 0
while i < 1 :#循环，除非关掉计算器，否则程序将一直继续
    def add(x,y):#加法
        return x + y

    def sub(x,y):#减法
        return x - y

    def mul(x,y):#乘法
        return x * y

    def div(x,y):#除法
        return x / y
#依次输入整数，运算符，整数
    num1 = int(input("输入数字后，按回车："))
    choice = input("输入运算符后按回车: ")
    num2 = int(input("输入数字后，按回车："))
#根据运算符，调用对应的函数，从而实现运算输出结果给用户
    if choice == '+':
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice == '-':
        print(num1,"-",num2,"=",sub(num1,num2))
    elif choice == '*':
        print(num1,"*",num2,"=",mul(num1,num2))
    elif choice == '/':
        print(num1,"/",num2,"=",div(num1,num2))
    else:
        print("出错啦")