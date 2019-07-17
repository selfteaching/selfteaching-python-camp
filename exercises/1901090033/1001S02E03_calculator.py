num1 = float(input("Enter num1 >> "))
num2 = float(input("Enter num2 >> "))
op = str(input("Enter operation (+, -, * or /) >>"))

if op == "+":
    result = str(num1 + num2)
elif op == "-":
    result = str(num1 - num2)
elif op == "*":
    result = str(num1 * num2)
elif op == "/":
    result = str(num1 * num2)
else:
    result = str("Invalid input")

