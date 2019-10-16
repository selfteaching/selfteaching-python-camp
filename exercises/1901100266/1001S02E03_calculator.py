num1 = float(input("Enter Number 1 >> "))
num2 = float(input("Enter Number 2 >> "))
opp = str(input("Enter Opperation (+, -, * or /) >>"))

if opp == "+":
    total = str(num1 + num2)
elif opp == "-":
    total = str(num1 - num2)
elif opp == "*":
    total = str(num1 * num2)
elif opp == "/":
    total = str(num1 / num2)
else:
    total = str("Unkown Opperation or Number")

print(total)