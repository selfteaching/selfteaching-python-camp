# def add(num1,num2):
#     return num1 + num2
# def sub(num1,num2):
#     return num1 - num2

# def mul(num1,num2):
#     return num1 * num2

# def div(num1,num2):
#     return num1 / num2

# print(div(1,1))
input('欢迎使用两位数计算器,你需要按照提示顺序依次输入数字或者符号,然后回车,按下回车开始:')
num1 = float(input('请输入需要计算的数字:'))
operator = input('请输入操作符(tip: + - * /):')
num2 = float(input('请输入需要计算的数字:'))
if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
