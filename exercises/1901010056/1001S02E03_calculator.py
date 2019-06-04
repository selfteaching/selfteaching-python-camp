def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+': 
        print('{} + {} = '.format(number_1, number_2))          # "if" expression ":" suite
                                                                # suite也可以放到和expression一行里
                                    
    elif operation == '-':                                      #"elif" expression ":" suite
        print('{} - {} = '.format(number_1, number_2))
        
    elif operation == '*':                                      #"elif" expression ":" suite
        print('{} * {} = '.format(number_1, number_2))
        
    elif operation == '/':                                      #"elif" expression ":" suite
        print('{} / {} = '.format(number_1, number_2))
        
    else:                                                       #"else" ":" suite
        print('You have not typed a valid operator, please run the program again.')

calculate()
