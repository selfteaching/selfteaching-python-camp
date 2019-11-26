operator = input('Please enter an operator（+,-,*,/):')
first_number = input('enter first number：')
second_number = input('enter second number：')

a = int(first_number)
b = int(second_number)

if operator =='+':
    print(a,'+',b,'=',a + b)
elif operator =='-':
    print(a,'-',b,'=',a - b)
elif operator =='*':
    print(a,'*',b,'=',a * b)
elif operator =='/':
    print(a,'/',b,'=',a / b)
else:
    print('Invalid operator')