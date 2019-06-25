print("Welcome to the calculator. ")

# define the function
# use input function to limit only run operation at time, if * then *
def calc():
    operation = input('''
Please type in wrong, you need to type +,-,*,/:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))
    # for + addition
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    # for subtration
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    # for multiplication
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    # for division
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed wrong, please run the program again.')

# add again function to calculator function        
    again()
# try to add again function when user need to use calculator again
def again():
    cal_again = input('''
Do you want to calculate again?
Please type Y FOR YES or N FOR NO.
''')
# if user type y or upper Y then run funciton of calculate
    if cal_again.upper() == 'Y':
        calculate()
# if user type n or upper N then print out byebye    
    elif cal_again.upper() == 'N':
         print('Bye Bye.')
# if run other words then run function of again  
    else:
        again() 


# Call calculate() outside of the function
calc()