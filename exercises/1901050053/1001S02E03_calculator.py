operator = input('''Please type in the math operation you would like to complete:
+ for addition
- for substraction
* for multiplication
/ for division
''')
number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))
if operator == '+':
    print('{} + {} = '.format(number_1 , number_2))
    print(number_1 + number_2)

elif operator == '-':
     print('{} - {} ='.format(number_1 , number_2))
     print(number_1 - number_2)

elif operator == '*':
      print('{} * {} = '.format(number_1,number_2))
      print(number_1 * number_2)

elif  operator == '/':  
      print('{} / {} = '.format(number_1,number_2))
      print(number_1 / number_2)

else :
    print('BAD LUCK! You have not typed a valid operator, please try again!')

          
