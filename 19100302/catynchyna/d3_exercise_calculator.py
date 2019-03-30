# Please show users some of our friendly aura...
def welcome():
    print("""\
Aloha, Welcome to Stitch Calculator!
""")

# how to set a function to call and restart again
# Define our function calculate()
def calculate():
    operation = input("""\
    Plese type in the math operation you want to conduct:
    + for Addition
    - for Substraction
    * for Multiplication
    / for Division
    """)

    number_1 = float(input("Enter your 1st number:  "))
    number_2 = float(input("Enter your 2nd number:  "))

    if operation == "+":
        print("{} + {} = ".format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == "-":
        print("{} - {} = ".format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == "*":
        print("{} * {} = ".format(number_1, number_2))
        print(number_1 * number_2)


    elif operation == "/":
        print("{} / {} = ".format(number_1, number_2))
# what if someone type in the 2nd number -- 0
        try:
            print(number_1 / number_2)
        except ZeroDivisionError:
            print("When using /, 2nd number cannot be zero. ")


    else:
        print("Sorry, we have not included this function yet. Please try again.")


# what if we wanna let user choose whether to proceed?
# Define a new function again() to ask whether user wanna try again
def again():

    calc_again = input("""\
    Do you wanna try again?
    Please type Y for YES or N for NO.
    """)

    # If user types Y, run the calculate() function
    # .upper to help provide user friendly inputing improvement
    if calc_again.upper() == "Y":
        calculate()

    # If user types N, byebye
    elif calc_again.upper() == "N":
        print("Ok, Have a nice day. Bye")

welcome()
calculate()
again()
# missed loopline need to be improved later. gogo cat!
