# this is d3 exercise, a calculator program
# date: 2019.3.20
# author by: qiming

#计算器程序
#定义欢迎语函数
def welcome():
    print("Welcome to Qiming's Calculator")
#定义加法函数
def add(a,b):
    return a+b
#定义减法函数
def substract(a,b):
    return a-b 
#定义乘法函数
def multiply(a,b):
    return a*b
#定义除法函数
def divide(a,b):
    return a/b
#定义计算器函数，实现输入、输出及运算
def calculator():
    #提示用户输入部分
    number_1 = int(input('Please enter your first number: '))
    operation = input('''Please select the math operation:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')
    number_2= int(input('Please enter your second number: '))
    #计算逻辑和输出结果部分
    #若选择加法
    if operation == '+' : 
        result = add(number_1,number_2)
        print('{}+{}='.format(number_1,number_2),result)
    #若选择减法
    elif operation == '-' : 
        result = substract(number_1,number_2)
        print('{}-{}='.format(number_1,number_2),result) 
    #若选择乘法
    elif operation == '*' :
        result = multiply(number_1,number_2) 
        print('{}*{}='.format(number_1,number_2),result)  
    #若选择除法
    elif operation == '/' :
        result = divide(number_1,number_2)
        print('{}/{}='.format(number_1,number_2),result)  
    #若超出选择范围
    else :
        print('opps, the calculator could not handle this.')
    again()
#定义重试函数
def again():
    try_again = input('''Do you wanna try again? Type "y" for Yes, "n" for No: ''')
    if try_again == 'y':
        calculator()
    elif try_again == 'n':
        print ('See you, my friend.')
    else:
        again()
#运行欢迎和计算器函数
welcome()
calculator()
