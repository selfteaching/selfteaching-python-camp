def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y


print("选择操作")
print("1.加法")
print("2.减法")
print("3.乘法")
print("4.除法")

choice = input("选择后回车，选择1/2/3/4：")

num1 = int(input("输入第一个数字后，按回车："))
num2 = int(input("输入第二个数字后，按回车："))

if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=",mul(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("输入错误")
    