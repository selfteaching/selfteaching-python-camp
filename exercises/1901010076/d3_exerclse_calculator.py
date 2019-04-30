# 这是邓超抄写的第一个简单程序
# 可以运算加减乘除的简易计算器

# 定义函数
def add(x, y):
    """相加"""

    return x + y

def subtract(x, y):
    """相减"""

    return x - y

def multiply(x, y):
    """相乘"""

    return x * y

def divide(x, y):
    """相除"""

    return x / y

# 用户输入
print("选择运算，")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")

num1 = int(input("请输入第一个数字："))

choice = input("请输入你的选择(1/2/3/4):")
num2 = int(input("请输入第二个数字："))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1,num2))
else:
    print("输入不正确")
    