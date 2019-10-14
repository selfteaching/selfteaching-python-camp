
operator = input('请输入运算符（+、-、*、/）：')
first_number = input('请输入第一个数字：')
seconde_number = input('请输入第二个数字：')

a = int(first_number)
b = int(seconde_number)

print('operator:', operator, type(operator))
print('first_number:', first_number, type(first_number), type(a))
print('second_number:', seconde_number, type(seconde_number), type(b))

if operator == '+':
    print(a, '+', b, '=', a + b)
elif operator == '-':
    print(a, '-', b, '=', a - b)
elif operator == '*':
    print(a, '*', b, '=', a * b)
elif operator == '/':
    print(a, '/', b, '=', a / b)
else:
    print('无效的运算符')