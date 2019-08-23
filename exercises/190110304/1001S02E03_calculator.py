
# This is a python language calculator

operator = input('Please enter an operator (+, -, *, /) : ')

a = int(first_number)
b = int(second_number)

if operator == '+':
    print(a, '+', b, '=', a + b)
elif operator == '-':
    print(a, '-', b, '=', a - b)  
elif operator == '*':
    print(a, '*', b, '=', a * b)  
elif operator == '/':
    print(a, '/', b, '=', a / b)
else:
    print('Null operator')    