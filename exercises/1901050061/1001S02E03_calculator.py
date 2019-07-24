output = 0
num1 = ""
operation = ""
num2 = ""
'''
In python, user input on the command line can be taken by using the command input(). 
Putting in a string (optional) as a paramter will give the user a prompt after which they can input text. 
This statement returns a string with the text the user typed, so it needs to be assigneed to a variable. 
This can be done in python like so, myvar = input("Feed me data! "). 
Python is not a language with strongly typed variables, which means that you do not have to define a type when you create a variable. 
The interpreter will automatically assign the variable a type the first time it is instantiated with data.

'''
'''
Getting input from the user for a calculation
This code will print a prompt asking for a first number to the screen, 
ask for input, print a prompt asking for an operation to the screen, ask for input, etc. 
The \n at the end of the strings is an escape character that tells python to add a newline to the end of the prompt.
I did this so that the user would start typing on the line below the prompt.
'''
num1 = input("Hello, What is your First Number?\n")
operation = input("Operation (+, -, *, /)?\n")
num2 = input("Your Second Number?\n")

'''
In order for us to do math on the numbers that the user typed,
we need to convert them to numerical values, as you cannot do math on strings, for obvious reasons.
(After all, what is "abc" / "def" anyways?) 
The method for doing so is called Typecasting. and in Python, 
you can convert to float (decimal numbers less than 7 digits) by using the float() statement. 
This can be done for our purposes like so,
'''
floatnum1 = float(num1)
floatnum2 = float(num2)

'''
Performing the math
'''
if operation == "+":
    output=floatnum1+floatnum2
if operation == "-":
    output=floatnum1-floatnum2
if operation == "*":
    output=floatnum1*floatnum2
if operation == "/":
    output=floatnum1/floatnum2
if operation == "+" or operation == "-" or operation == "/" or operation == "*":
	''' 
	Using the print() statement, we can print the result out to the screen. 
	In Python, strings can be concatenated by "adding" them together, as if they were numbers. 
	The code for this step looks like this: print("Your Answer: "+str(output)). 
	This code prints the text "Your answer: " concatenated with the output, after it has been typecasted to a string. 
	(You can't concatenate it while it is still formatted as a float)
	'''
	print("Your Answer: "+str(output))
else:
    print("Your operation is invalid, please try again")
