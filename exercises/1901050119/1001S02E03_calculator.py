def add(x, y):
    return x + y

def substract(x, y):
    return x-y
    
def mutiply(x, y):
    return x*y

def divide(x, y):
    return x/y

aDict = {"+": 1, "-": 2, "*": 3, "/": 4}
operator = input("请选择运算类型：+、-、*、/")

if operator in aDict:
    a = int(input("请输入第一个数字："))
    b = int(input("请输入第二个数字："))
    if operator == '+':
        print(add(a, b))
    elif operator == '-':
        print(substract(a, b))
    elif operator == '*':
        print(mutiply(a, b))
    elif operator == '/' and b != 0:
        print(divide(a, b))
    else:
        print("除数不能为零！")
else:
    print("输入错误！") 