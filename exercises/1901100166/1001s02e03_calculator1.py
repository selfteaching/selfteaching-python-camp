fuhao = input("请输入运算符号(+,-,*,/):")
a=int(input("请输入第一个数字"))
b=int(input("请输入第二个数字"))

if fuhao == '+':
    print(a + b)
elif fuhao == '-':
    print(a - b)
elif fuhao == '*':
    print(a * b)
elif fuhao == '/':
    print(a / b)
else:
    print('无效的运算符')