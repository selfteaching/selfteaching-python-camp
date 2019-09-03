#用户输入
print("欢迎使用python计算机！")
print("请输入数字，选择自己的需求。/ 1.相加 2、相减 3、相乘 4、相除   列如：1")

#定义加减乘除的函数
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

#判断输入的要求
choice = input("输入你的选择：")
f1 = choice
if f1=='1':
    num1 = float(input("输入第一个数字："))
    num2 = float(input("输入第二个数字："))

elif f1=='2':
    num1 = float(input("输入第一个数字："))
    num2 = float(input("输入第二个数字："))

elif f1=='3':
    num1 = float(input("输入第一个数字："))
    num2 = float(input("输入第二个数字："))

elif f1=='4':
    num1 = float(input("输入第一个数字："))
    num2 = float(input("输入第二个数字："))
else:
    print('非法操作')


#实现要求
if choice == '1':
    print(num1,"+",num2," = ",add(num1,num2))

elif choice == '2':
    print(num1,"-",num2," = ",subtract(num1,num2))

elif choice == '3':
    print(num1,"x",num2," = ",multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2," = ",divide(num1,num2))

else:
    print("输出有误")