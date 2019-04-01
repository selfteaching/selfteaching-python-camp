#这是一个实现为计算器的程序
a = 0#创建一个int型变量
b = 0#创建一个int型变量
x = "+" #创建一个字符型变量
a = float(input('请输入第一个数')) #获取输入内容并转化为浮点数
b = float(input('请输入第二个数')) #获取输入内容并转化为浮点数
x = input('请输入运算符, = 号退出') #获取输入内容
while x != "=":  #连续输入及退出的循环
    if x == "+": #对运算类型的判断
        print(a+b)
        a = a+b
    elif x == "-": #对运算类型的判断
        print(a-b)
        a = a-b
    elif x == "*": #对运算类型的判断
        print(a*b)
        a = a*b
    elif x == "/": #对运算类型的判断
        print(a/b)
        a = a/b
    elif x == "**": #对运算类型的判断
        print(a**b)
        a = a**b
    a = float(input("请输入下一个数"))#获取输入内容并转化为浮点数
    b = float(input('请输入下一个数')) #获取输入内容并转化为浮点数
    x = input('请输入运算符, = 号退出') #获取输入内容
