# 这是一个只能进行加减乘除运算的初级计算器程序
# 提示用户输入运算符，判断是否正确输入，并将数值存入对应变量
while True:
    operator = input('请输入运算符（+、-、*、/）: ')
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        break
    else:
        print('请输入正确的运算符')
        continue
# 提示用户输入数字，判断是否正确输入，并将数值存入对应变量
while True:
    Number_One = input('请输入第一个数字：')
    if Number_One.isdigit():
        break
    else:
        print('请输入正确的数字')
        continue
while True:
    Number_Two = input('请输入第二个数字：')
    if Number_Two.isdigit():
        break
    else:
        print('请输入正确的数字')
        continue       
# 将数字变量的字符类型由'Str'转换为'Int'
a = int(Number_One)
b = int(Number_Two)

# 按运算规则进行运算并输出结果
if operator == '+':
    print(a,'+',b,'=',a + b)
elif operator == '-':
    print(a,'-',b,'=',a - b)
elif operator == '*':
    print(a,'*',b,'=',a * b)   
elif operator == '/':
    print(a,'÷',b,'=',a / b)