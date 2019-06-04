# Young4's first calculator in Python
def welcome():
    print('''
    Welcome to Young4's Calculator
    ''')

def calculate():
    
    number_1 = int(input('Please enter your first number: '))
    number_2 = int(input('Please enter your second number: '))
    
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    #Addition
    if operation == '+':
        print('{} + {}= '.format(number_1,number_2))
        print(number_1 + number_2)

    #Subtaction
    elif operation == '-':
        print('{} - {}= '.format(number_1,number_2))
        print(number_1-number_2)
        
    #Mutiplication
    elif operation == '*':
        print('{} * {}= '.format(number_1,number_2))
        print(number_1 * number_2)

    #Division
    elif operation == '/':
        print('{} / {}= '.format(number_1,number_2))
        print(number_1 / number_2)

    else:
        print('You have not type a valid operator, please run the program again')
    
    #Add again() function to calculate() function
    again()

def again():

    #take input from user
    calc_agin = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')

    #If user types Y, run the calculate() function
    #Accept 'y' or 'Y' by adding str.upper()
    if calc_agin.upper() == 'Y':
        calculate()

    #If user types N , say good-bye to the user and end the program
    #Accept 'n' or 'N' by adding str.upper()
    elif calc_agin.upper() == 'N':
        print('See you later.')

    #If user types another key, run the function again
    else:
        again()

#Call welcome() and calculate() outside of the function
welcome()
calculate()