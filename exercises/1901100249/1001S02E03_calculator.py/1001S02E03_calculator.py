# Progam make a simple calculator that can add,subtract,mutiply and divide using functions
# This function adds two numbers
def add(x,y):
    return x + y
# This function subtracts two mumbers
def subtract(x, y):
    return x - y
# This funtion multiplies two numbers
def multiplie(x, y):
    return x * y
# This function divides two numbers
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# Take input from the user
Choice = input("Enter choice（1/2/3/4）:")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if Choice == '1':
    print(num1,'+',num2,'=',add(num1,num2))
elif choice == '2':
    print(num1,'-',num2,'=',subtract(num1,num2))
elif Choice == '3':
    print(num1,'*',num2,"=",multiply(num1,num2))
elif Choice =='4':
    print(num1,'/',num2,'=',divide(num1,num2))
else:
    print("Invalid input")
    