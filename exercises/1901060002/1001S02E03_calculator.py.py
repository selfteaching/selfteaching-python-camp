num1 = int(input('Enter one number: '))
num2 = int(input('Enter another number: '))
operation = input("Enter operation\n[+,-,*,/]")
if operation == '+':
    sum = num1 + num2
elif operation == '-':
    sum = num1 - num2
elif operation == '*':
    sum = num1 * num2
else:
    sum = num1 / num2
print(sum)

