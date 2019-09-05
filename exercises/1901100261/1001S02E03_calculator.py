# Program make a simple calculator that can add, subtract, multiply and dicide using functions

# #Pode是一个简单的计算器，可以使用函数进行加，减，乘和自杀

 adds two numbers
def add(x, y):
    return x + y

# subtracts two numbers This function
def subtract(x, y):
    return x - y 

# This function multiplies two numbers
def multiply(x, y):
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
choice = input("Enter choice(1/2/3/4):")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=",multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Invalid input") 

    