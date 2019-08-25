# 定义函数
def add(x,y):
    "”“相加”“”
    return x + y

def subtract(x,y):
    """相减"""
    return x - y

def multiply(x,y):
    """相乘"""
    return x * y

def divide(x,y):
    """相除"""
    return x / y

# 用户输入
peint("选择运算:")
print("A、相加")
print("B、相减")
print("C、相乘")
print("D、相除")

choice = input("请选择（A/B/C/D):")
num1 = int(input("输入第一个数字"))
num2 = int(input("输入第二个数字"))

if choice == 'A':
    print(num1,"+",num2,"=",add(num1,num2))

elif choice == 'B':
    print(num1,"-",num2,"=",subtract(num1,num2))

elif choice == 'C':
    print(num1,"*",num2,"=",multiply(num1,num2))

elif choice == 'D':
    print(num1,"/",num2,"="divide)(num1,num2))
else:
    print("无法计算")