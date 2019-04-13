# Below is a simple calculator which can perform adding, substracting, multipling, dividing, getting quotient, or getting remainder from the two numbers entered by user
# Firstly create functions for operations
def add (x,y):
    return x+y
def substract (x,y):
    return x-y
def multiple (x,y):
    return x*y
def divide (x,y):
    return x/y
def quotient (x,y):
    return x//y
def reminder (x,y):
    return x%y

# Then build the blocks for user to provide inputs
print("Please type in 2 numbers you would like to use for calculation.")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
a = num1
b = num2
print("Please select the operation (A/B/C/D/E/F) you would like to perform from below list.")
print("A. add \nB. substract \nC. multiple \nD. divide \nE. get quotient \nF. get reminder")
choice = input("Enter your choice of operation: ")

# Lastly process the inputs from user to do the corresponding calculation
if choice == "A":
    print(a,"plus",b,"equals to ",add(a,b))
elif choice == "B":
    print(a,"minus",b,"equals to ",substract(a,b))
elif choice == "C":
    print(a,"multiple",b,"equals to ",multiple(a,b))
elif choice == "D":
    print(a,"divide",b,"equals to ",divide(a,b))
elif choice == "E":
    print("The quotient of ",a,"and",b,"equals to ",quotient(a,b))
elif choice == "F":
    print("The reminder of ",a,"divided by",b,"equals to ",reminder(a,b))
else:
    print("Oops, there\'s something wrong with your inputs, please try again :)") 







