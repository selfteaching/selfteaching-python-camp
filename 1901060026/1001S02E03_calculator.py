# Filename : calculator.py
# Author by : Evans

# Define the function
def add (x , y):
    """add"""
    return x + y

def subtract(x , y):
    """subtract"""
    return x - y

def multiply(x , y):
    """muliply"""
    return x * y

def divide(x , y) :
    """divide"""
    return x / y

# User input
print("Choose function")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Input your choice(1/2/3/4):")

num1 = float(input("Input the first number:"))
num2 = float(input("Input the second number"))

if choice == '1' :
    print(num1,"+",num2,"=",add(num1,num2))

elif choice =='2' :
    print(num1,"-",num2,"=",subtract(num1,num2))

elif choice =='3' :
    print(num1,"*",num2,"=",multiply(num1,num2))

elif choice =='4' :
    print(num1,"/",num2,"=",divide(num1,num2))

else:
    print("Error")
