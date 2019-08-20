operator = input('Please enter an operator (+, -, *, /) : ')
first_number = input('Please enter the first number : ')
second_number = input('Please enter the second number : ')

a=int(first_number)
b=int(second_number)

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
