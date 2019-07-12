def calculate():
     operation = input('''
     please type in the math operation you would like to complete:
     + for addition
     - for subtraction
     * for multiplication
     / for division
     ''')
     number_1 = float(input('Please enter the first number: '))
     number_2 = float(input('Please enter the second number: '))
     if operation == '+': 
          print('{} + {} = {} '.format(number_1, number_2,number_1 + number_2))          
                                    
     elif operation == '-':
          print('{} - {} = {} '.format(number_1,number_2,number_1 - number_2))
     elif operation == '*':                                      
          print('{} * {} = {} '.format(number_1, number_2,number_1 * number_2))
     elif operation == '/' and number_2 != 0:                                      
          print('{} / {} = {} '.format(number_1, number_2,number_1 / number_2))
     else:
          print('You have not typed a valid operator, please run the program again.')


calculate()
