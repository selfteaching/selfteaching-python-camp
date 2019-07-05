# For implementing a calculator can do + - * /

# first number input
number1 = input("input a number1: ")
number1 = float(number1)
# selection one from + - * /
operator = input("input a operator from +, -, *, / : ")
# second number input
number2 = input("input a number2: ")
number2 = float(number2)
# calculator
if operator == '+':
    addtion = number1 + number2
    print('{:} + {:} = {:f}'.format(number1, number2, addtion))
if operator == '-':
    subtraction = number1 - number2
    print('{:} - {:} = {:f}'.format(number1, number2, subtraction)) 
if operator == '*':
    multiplication = number1 * number2
    print('{:} * {:} = {:f}'.format(number1, number2, multiplication)) 
if operator =='/':
    try:
        division = number1 / number2
    except:
        print('The denominator: number2 cannot be 0 when divison being done.')# denominator cannot be zero
    else:
        print('{:} / {:} = {:f}'.format(number1, number2, division)) 
