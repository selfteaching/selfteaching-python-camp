#简易加减乘除计算器程序
#定义加法函数
def add(x,y)：
    return x+y
#定义减法函数
def substract（x，y）：
    return x-y
#定义乘法函数
def multiply（x，y）：
    return x*y
#定义除法函数
def divide（x，y）：
    return x/y
#定义执行方式，当执行脚本本身，执行如下代码
if __name__ == '__main__':               
    print("******************************")
    print("          计算器")
    print("******************************")
    chose = input("选择你要的计算方式，1/加法 ，2/减法，3/乘法，4/除法: ")
    if chose == "1":
        tmp = input("请输入你要计算的数字:")
        add(tmp)
    elif chose == '2':
        tmp = input("请输入你要计算的数字:")
        subtraction(tmp)
    elif chose == '3':
        tmp = input("请输入你要计算的数字:")
        multiplication(tmp)
    elif chose == '4':
        tmp = input("请输入你要计算的数字:")
        division(tmp)
    else:
        print("你输入的有误，请重新输入")

