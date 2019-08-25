# Calculator

Operator=input('Pls input a operator (+, -, *, / ): ')
First_number=input ('Pls input the first number: ')
Second_number=input('Pls input the second number: ')

a=int(First_number)
b=int(Second_number)

if (Operator == '+'):
    print(a, '+', b , '=', a+b)
elif (Operator == '-'):
    print(a, '-', b , '=', a-b)
elif (Operator == '*'):
    print(a, '*', b , '=', a*b)
elif (Operator == '/'):
    print(a, '/', b , '=', a/b)
else:
    print ('invalid inputs')