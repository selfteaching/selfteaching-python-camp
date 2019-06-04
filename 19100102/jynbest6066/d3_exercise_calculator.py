
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

calculator = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if calculator == '1':
    print('result:', add(num1, num2))
elif calculator == '2':
    print('result:', subtract(num1, num2))
elif calculator == '3':
    print('result:', multiply(num1, num2))
elif calculator == '4':
    print ('result:', divide(num1, num2))
else:
    print("Invalid input")
