operation=input('''请输入您想进行的运算操作：
+ 加
- 减
* 乘
/ 除
''')

#提示输入数值
number_1 = float(input('enter your first number: '))
number_2 = float(input('enter your second number: '))

#定义加法
if operation =='+':
    print('{}+{}= '.format(number_1,number_2))
    print(number_1 + number_2)


#定义减法
elif operation == '-':
    print('{}-{}= '.format(number_1,number_2))
    print(number_1-number_2)

#定义乘法
elif operation =='*':
    print('{}*{}= '.format(number_1,number_2))
    print(number_1*number_2)

#定义除法
elif operation =='/':
    print('{}/{}= '.format(number_1,number_2))
    print(number_1/number_2)

#其他情况
else:
    print("oh, you have to do it again")