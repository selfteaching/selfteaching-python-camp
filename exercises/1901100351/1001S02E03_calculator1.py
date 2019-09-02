operation=input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division

''')#用'''输入分段内容
nubmber_1=float(input('Enter your first number:'))#输入第一个浮点数值
nubmber_2=float(input('Enter your second number:'))#输入第二个浮点数值
if operation=='+':
    print('{}+{}='.format(nubmber_1,nubmber_2))#‘{}+{}=’.format()表示按默认顺序的格式化函数

''')
nubmber_1=float(input('Enter your first number:'))
nubmber_2=float(input('Enter your second number:'))
if operation=='+':
    print('{}+{}='.format(nubmber_1,nubmber_2))

    print(nubmber_1+nubmber_2)
elif operation=='-':
    print('{}-{}='.format(nubmber_1,nubmber_2))
    print(nubmber_1-nubmber_2)
elif operation=='*':
    print('{}*{}='.format(nubmber_1,nubmber_2))
    print(nubmber_1*nubmber_2)
elif operation=='/':
    print('{}/{}='.format(nubmber_1,nubmber_2))
    print(nubmber_1/nubmber_2)
else:
    print('You have not typed a valid operator,please run the program again.')