def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def multi(x,y):
    return x * y

def div(x,y):
    return x / y

print("选择运算：\n1、相加\n2、相减\n3、相乘\n4、相除")

choice = input("输入你的选择（1/2/3/4）：")
num1 = int(input("输入第一个数字："))
num2 = int(input("输入第二个数字："))

if choice == '1':
    print(num1,"+",num2, "=",add(num1,num2))
elif choice == '2':
    print(num1,"-",num2, "=",sub(num1,num2))
elif choice == '3':
    print(num1,"*",num2, "=",multi(num1,num2))
elif choice == '4':
    print(num1,"/",num2, "=",div(num1,num2))
else:
    print("非法输入")
