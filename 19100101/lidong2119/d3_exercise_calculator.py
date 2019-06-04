numA = float(input('Please enter a number: '))
op = input('Please enter a operator: ')
numB = float(input('Please enter another number: '))
if op == '+':
    print("result: ",numA+numB)
elif op == '-':
    print("result: ",numA-numB)
elif op == '*':
    print("result: ",numA*numB)
elif op == '/':
    print("result: ",numA/numB)
else:
    print("Unknown operator ",op)