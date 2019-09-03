# program make a simple calculator that can add,subtract,
# multipl and divide
# This fuction adds two numbers
def add(x,y):
    return x + y
# This fuction subtract two numbers
def subtract(x,y):
    return x - y
# This fuction multiply two numbers
def multiply(x,y):
    return x * y
# This fuction divide two numbers
def divide(x,y):
    return x / y

print("select operation.")
print("1:add")
print("2:subtract")
print("3:multiply")
print("4:divide")

# Take input from the user
choice = input("Enter your choice(1/2/3/4):")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid input") 