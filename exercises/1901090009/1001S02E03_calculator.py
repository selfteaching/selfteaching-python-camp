print("please choose the calculation method: ")
print("1'add")
print("2'subtract")
print("3'multiply")
print("4'divide")

choice = input("please enter the serial number of calculation method: ")

number1 = int(input("please enter the first number: "))
number2 = int(input("please enter the second number: "))

if choice == '1':
    print(number1, "+", number2, "=", number1 + number2)
elif choice == '2':
    print(number1, "-", number2, "=", number1 - number2)
elif choice == '3':
    print(number1, "*", number2, "=", number1 * number2)
elif choice == '4':
    print(number1, "/", number2, "=", number1 / number2)
else:
    print("error")