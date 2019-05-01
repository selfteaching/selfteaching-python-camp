"""
Created on Sat Apr 13 11:19:46 2019

@author: PetalSaya
"""

# Program
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def devide(x, y):
    return x / y

def calcultate ():    
# User input
    input('''Hello, welcome to petalsaya calculator! 
Press 'Enter' to begin.''')
    num1 = float (input("Enter first number: "))
    choice = input ("Enter operation (+,-,*,/):")
    num2 = float (input("Enter second number: "))

    if choice == '+':
        print (add (num1, num2))
    elif choice == '-':
        print (subtract (num1, num2))
    elif choice == '*':
        print (multiply (num1, num2))
    elif choice == '/':
        print (devide (num1, num2))
    else:
        print ("Invalid input")

def again():
# User input
    calc_again = input ("Do you want to calculate again? Y/N.")
    if calc_again == 'Y':
        calcultate()
    elif calc_again == 'N':
        print ("See you later.")
    else:
        again()

# Operation 
calcultate()
again ()




