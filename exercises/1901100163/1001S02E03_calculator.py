#Calculator used by Python
def add(x,y): #加法
    return x+y
def subtrac(x,y): #减法
    return x-y
def multiply(x,y): #乘法
    return x*y
def divide(x,y): #除法
    return x/y
#用户输入
print("选择运算：")
print("用户选择1、相加")
print("用户选择2、相减")
print("用户选择3、相乘")
print("用户选择4、相除")
choice=input("输入你的选择1/2/3/4:")
num1=float(input("第一个数字："))
num2=float(input("第二个数字："))
if choice=="1":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=="2":
    print(num1,"-",num2,"=",subtrac(num1,num2))
elif choice=="3":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=="4":
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("非法输入")