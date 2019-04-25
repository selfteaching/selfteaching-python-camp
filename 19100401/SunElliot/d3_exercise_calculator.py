# Python program for simple calculator

# Function to add two numbers 

def  add(num1,num2):
    return num1 + num2

# Function to subtract two numbers 
def substract(num1,num2):
    return num1 - num2

# Function to mutiply two numbers 
def multipfy(num1,num2):
    return num1 * num2

# Function to devide two numbers 
def divide(num1,num2):
    return num1 / num2

print("Please select operation -\n"\
    "1.Add\n"\
    "2.Subtract\n"\
    "3.Multiply\n"\
    "4.Devide\n")
#Take input from the user 

select = input("Select operations from 1,2,3,4:")

number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))


if select =='1':
    print(number_1,"+",number_2,"=",
                    add(number_1,number_2) )
elif select =='2':
    print(number_1,"+",number_2,"=",
                    substract(number_1,number_2) )
elif select =='3':
    print(number_1,"+",number_2,"=",
                    multipfy(number_1,number_2) )
elif select =='4':
    print(number_1,"+",number_2,"=",
                    divide(number_1,number_2) )
else:
    print("Invalid input")