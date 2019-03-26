#定义函数
#加法
def add(x,y):
    return x + y
#减法
def subtract(x,y):
    return x - y
#乘法
def multiply(x,y):
    return x * y
#除法
def divide(x,y):
    return x / y
#用户输入
print('选择运算:')
print('1、加法')
print('2、减法')
print('3、乘法')
print('4、除法')
choice = input('请输入您的选择1/2/3/4：')   #任何输入都必须要有个变量名来接收
number1 = int(input('输入第一个数：'))
number2 = int(input('输入第二个数：'))
if choice == '1':
    print(number1,"+" ,number2,"=",add(number1,number2) )
elif choice == '2':
    print(number1,"-" ,number2,"=",subtract(number1,number2) )
elif choice == '3':
    print(number1,"*" ,number2,"=",multiply(number1,number2) )
elif choice == '4':
    print(number1,"/" ,number2,"=",divide(number1,number2) )
else:
    print('非法输入')      #第一次操作，编程bug不断，哈哈，精进，加油
    #难道用中文名提交，有冲突吗？