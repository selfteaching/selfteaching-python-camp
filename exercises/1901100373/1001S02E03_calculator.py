first_number = float(input('Please enter the first number '))
second_number = float(input('Please enter the second number '))
calculation = input(
    'Please enter which one of the calculation you want to make between the two numbers: "+", "-", "*", or "/" ')
if calculation == '+':
    print('Result is ', (first_number+second_number))
elif calculation == '-':
    print('Result is ', (first_number-second_number))
elif calculation == '*':
    print('Result is ', (first_number*second_number))
else:
    print('Result is ', (first_number/second_number))
