# Define functions
def Addition(x, y):
   """Addition"""
 
   return x + y
 
def Subtraction(x, y):
   """Subtraction"""
 
   return x - y
 
def Multiplication(x, y):
   """Multiplication"""
   
   return x * y
 
def Division(x, y):
   """Division"""
 
   return x / y
 
# Input from Keyboard
print("Which math operation do you like to run：")
print("1、Addition")
print("2、Substration")
print("3、Multification")
print("4、Division")
 
choice = input("Input your selection(1/2/3/4):")
 
number_1 = float(input("'Enter your 1st number: "))
number_2 = float(input("'Enter your 2nd number: "))
 
if choice == '1':
   print(number_1,"+",number_2,"=", Addition(number_1,number_2))
 
elif choice == '2':
   print(number_1,"-",number_2,"=", Subtraction(number_1,number_2))
 
elif choice == '3':
   print(number_1,"*",number_2,"=", Multiplication(number_1,number_2))
 
elif choice == '4':
   print(number_1,"/",number_2,"=", Division(number_1,number_2))
else:
   print("You did not key-in a valid math operation!")