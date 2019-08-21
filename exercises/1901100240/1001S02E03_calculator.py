print("This is a designed calculator")

# THis part is to collect the input of numbers and operations. And report error if the input is illegal
while True:
    try:
        a=float(input("Please enter the first number"))
        break
    except ValueError:
        print("Error! You should enter a numbenr!")
while True:
    b=input("Enter the operation you want do. Type in one of the '+', '-', '*', '/'")
    if b in ['+','-','*','/']:
        break
    else:
        print("Error! You should type in one of '+', '-', '*', '/'")
while True:
    try:
        c=float(input("Please enter the second number"))
        break
    except ValueError:
        print("Error! You should enter a numbenr!")

# This part is doing the calculation by checking the value of b.
if b=='+':
    print("The result of calculation is ", a+c)
elif b=='-':
    print("The result of calculation is ", a-c)
elif b=='*':
    print("The result of calculation is ", a*c)
elif b=='/': # This part is doing the division and dealing with the ZeroDivision Error.
    while c==0:
        print("Error! The denominator can't be zero, this will cause a ZeroDivision Error!")
        while True:
            try:
                c=float(input("Please enter the second number"))
                break
            except ValueError:
                print("Error! You should enter a numbenr!")
    print("The result of calculation is ", a/c)

        