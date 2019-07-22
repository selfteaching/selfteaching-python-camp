def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

print("PLEASE CHOOSE THE CALCULATION METHOD: ")
print("1'ADD")
print("2'SUBTRACT")
print("3'MULTIPLY")
print("4'DIVIDE")

choice = input("PLEASE ENTER THE SERIAL NUMBER OF CALCULATION METHOD: ")

number1 = int(input("PLEASE ENTER THE FIRST NUMBER: "))
number2 = int(input("PLEASE ENTER THE SECOND NUMBER: "))

if choice == '1':
    print(number1, "+", number2, "=", add(number1,number2))
elif choice == '2':
    print(number1, "-", number2, "=", subtract(number1,number2))
elif choice == '3':
    print(number1, "*", number2, "=", multiply(number1,number2))
elif choice == '4':
    print(number1, "/", number2, "=", divide(number1,number2))
else:
    print("ERROR")