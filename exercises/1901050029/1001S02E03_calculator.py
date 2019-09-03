# Filename : 1001S02E03_calculator
# author by : 张金磊

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

########################################################
status = 1

# 用户输入
print("选择运算：")
print("1、相加","2、相减","3、相乘","4、相除")
print("\n")

choice = input("输入你的选择(1/2/3/4):")
choice_int = int(choice)


if choice_int > 4:
    status = 0
    print("非法输入")
    
    

if(status == 1):
    num1 = int(input("输入第一个数字: "))
    num2 = int(input("输入第二个数字: "))
    
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
    
    

