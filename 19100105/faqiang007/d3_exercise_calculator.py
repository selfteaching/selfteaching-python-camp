#定义加法
def add(x,y):
    '+'
    return x + y

#定义减法
def subtract(x,y):
    '-'
    return x - y

#定义乘法
def divide(x,y):
    '*'
    return x * y

#定义除法
def divide(x,y):
    '/'
    return x / y

print("请选择运算")
print("1,加法运算")
print("2,减法运算")
print("3,乘法运算")
print("4,除法运算")

choice = input("请输入要进行的运算：1、2、3、4")

num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))

#进行运算
if choice == '1':
   print(num1,"+"，num2，"="add(num1,num2),)

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))

else:
    print("非法输入")