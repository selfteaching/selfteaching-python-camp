num1 = int(input("Enter a number:"))
op = input('Enter Operator')
num2 = int(input("Enter another number:"))

if op == "+":
    print(num1 + num2)

elif op == '-':
    print(num1 - num2)

elif op == "*":
    print(num1 * num2)

elif op == "/":
    print(num1 / num2)

else:
    print("invalid operator") 

