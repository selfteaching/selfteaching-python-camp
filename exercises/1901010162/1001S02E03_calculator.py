# 2个数字相加
def add(x, y):
    return x+y

# 2个数字相减
def subtract(x, y):
    return x-y

# 2个数字几相乘
def multiply(x, y):
    return x * y

# 2个数字相除
def divide(x, y):
    return x / y

# 用户功能
print("计算器功能列表")
print("1.加法")
print("2.减法")
print("3.乘法")
print("4.除法")

# 用户操作
choice = input("(1/2/3/4)输入对应序号:")

num1 =float ( input("输入第一个数字:"))
num2 =float( input("输入第二个数字:"))

if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
 
elif choice == '2':
    print(num1,"-",num2,"=",subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=",multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("输入错误，请重试")