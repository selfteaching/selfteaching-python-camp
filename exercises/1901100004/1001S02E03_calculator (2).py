operator = input
first_numbder = input
secod_number = input

a = int(first_numder)
b = int(second_number)

print('operator:',operator,type(operator))
print('first_number:',first_numbder,type(first_numbder),type(a))
print('second_numder:',secod_number,type(secod_number),type(b))

print('测试加法 str 加法：'，first_number + secod_number)



if operator == '+':
    print(a, '+', b, '=',a + b)
elif operator == '-':
    print(a,'-', b, '=', a - b)
elif operator == '*':
    print(a, '*', b, '=', a * b)
elif operator == '/':
    print(a, '/', b, '=', a / b)
else:
    print('无效运算符')