num1 = int(input("please enter a num1"))
Op = input("operator")
num2 = int(input("please enter a num2"))

if Op == "+":
    print(eval(num1 + num2))

elif Op == '-':
    print(num1 - num2)

elif Op == "*":
    print(num1 * num2)

elif Op == "/":
    print(num1 / num2)

