operator = input('Please input operator(+,-,*,/):') #hint while waiting for value input
first_number = input('Please input first number:')
second_number = input('Please input second number:')

a = int(first_number) # convert string(str) to integer(int) for calculation
b = int(second_number)

print('operator', operator, type(operator))
print('first_number', first_number, type(first_number), type(a))
print('second_number', second_number, type(second_number), type(b))

print('test str addition', first_number + second_number)
#print('test str subtraction', first_number - second_number) 

if operator == '+':
    print(a, '+', b, '=', a + b) #a comma after every var
elif operator == '-':
    print(a, '-', b, '=', a - b)
elif operator == '*':
    print(a, '*', b, '=', a * b)
elif operator == '/':
    print(a, '/', b, '=', a / b )
else:
    print('ValueError')



