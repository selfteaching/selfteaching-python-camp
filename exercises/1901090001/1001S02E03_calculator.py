
num1 = float(input("Enter num1 >> "))
num2 = float(input("Enter num2 >> "))
opp = str(input("Enter Opperation (+, -, * or /) >>"))

if opp == "+":
   result = str(num1 + num2)
elif opp == "-":
   result = str(num1 - num2)
elif opp == "*":
   result = str(num1 * num2)
elif opp == "/":
   result = str(num1 / num2)
else:
   result = str("Invalid input")

print(result)