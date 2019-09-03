# 定义函数
def add(x,y):
    """加"""
    return x + y

def subtract(x,y):
    """减"""
    return x - y

def multiply(x,y):
    """乘"""
    return x * y

def divide(x,y):
    """除"""
    return x / y

# 用户输入
print("选择运算:")
print("1.加")
print("2.减")
print("3.乘")
print("4.除")

choice = input("choice（1/2/3/4):")
num1 = int(input("num1:"))
num2 = int(input("num2:"))

if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=",subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=",multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print('输入错误')
