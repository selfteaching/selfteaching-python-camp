# This is a simple calculator can only calculate four basic algorithm
print("This is a designed calculator")

# THis part is to collect the input of numbers and operations
# Report error if the input is illegal by using try and except
# While loop will not stop until enter a ligal statement
while True:
    # Restrict the input in form of float or int
    try:
        a=float(input("Please enter the first number: "))
        break
    # Provide a feed back and ask for re enter
    except ValueError:
        print("Error! You should enter a numbenr!")
while True:
    # Restrict the input in form of +, -, *, /
    b=input('''Please type in the operation you want to complete: 
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')
    # Break the loop if input is legal
    if b in ['+','-','*','/']:
        break
    # Provide the feedback if input is illegal
    else:
        print("Error! You should type in one of '+', '-', '*', '/'")
# Check the legality for the second input number
while True:
    try:
        c=float(input("Please enter the second number: "))
        break
    except ValueError:
        print("Error! You should enter a numbenr!")

# Doing the calculation by combining the imformation in a, b, c
# For addition case
if b=='+':
    print("The result of calculation is: \n", a,' + ',c,' = ',a+c)
# For subtraction case
elif b=='-':
    print("The result of calculation is ", a,' - ',c,' = ',a-c)
# For multiplication case
elif b=='*':
    print("The result of calculation is ", a,' * ',c,' = ',a*c)
# For division case
elif b=='/':
    while c==0:     # Check if the denominator is zero
        print("Error! The denominator can't be zero, this will cause a ZeroDivision Error!")
        # Ask for new denominator number
        while True:
            try:
                c=float(input("Please enter the second number"))
                break
            except ValueError:
                print("Error! You should enter a numbenr!")
    print("The result of calculation is ", a,' / ',c,' = ', a/c)

        