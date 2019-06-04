

i = int(input('请输入一个整数: '))
x = int(input('请再输入一个整数: '))
operation = input('''\
请输入要进行的运算符号（注：+ 代表"加法", - 代表"减法", * 代表"乘法", / 代表"除法"）: ''')

if operation == '+':
    print('{} + {} = '.format(i, x))
    print(i + x)

elif operation == '-':
    print('{} - {} = '.format(i, x))
    print(i - x)

elif operation == '*':
    print('{} * {} = '.format(i, x))
    print(i * x)

elif operation == '/':
    print('{} / {} = '.format(i, x))
    print(i / x)

else:
    print('抱歉，您输入了非法的运算符，请重新运行本程序')
    