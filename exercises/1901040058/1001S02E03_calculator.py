#四个函数调用add(加法)、subtract（减法）、multiply（乘法）、divide(除法)
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
#界面
print('select operation') 
print('1.add')
print('2.subtract')
print('3.multiply')
print('4.divide')

choice = input ("enter choice(1/2/3/4):") #用来选择加减乘除法
num1 = int(input("enter first number: ")) #用来输入数字
num2 = int(input("enter second number: "))
#使用多分支选择结构（if elif else)
if choice == '1':
    print(num1,'+',num2,'=', add(num1,num2))

elif choice == '2':
    print(num1,'-',num2,'=', subtract(num1,num2))

elif choice == '3':
    print(num1,'*',num2,'=', multiply(num1,num2))
elif choice == '4' and num2 != 0: #考虑除数为0的情况
    print(num1,'/',num2,'=', divide(num1,num2))
else:
    print("invalid input")
