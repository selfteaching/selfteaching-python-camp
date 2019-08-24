def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

print("Please choose the calculation method:")
print("1'ADD")
print("2'SUBSTRACT")
print("3'MULTIPLY")
print("4'DIVIDE")

choice = input("Please enter the serial number of calculation method: ")

number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number:"))

if choice == '1':
    print(number1, "+", number2, "=", add(number1, number2))
elif choice == '2':
    print(number1, "-", number2, "=", subtract(number1, number2))
elif choice == '3':
    print(number1, "*", number2, "=", multiply(number1, number2))
elif choice == '4':
    print(number1, "/", number2, "=", divide(number1, number2))
else:
    print("ERROR")
