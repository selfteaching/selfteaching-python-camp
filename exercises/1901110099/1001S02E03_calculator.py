def calculation():
    operation=input('''
Please type in the math type you want to operate:
+ for add
- for abtract
* for multiply
/ for divide
''')

    number_1=int(input('please type the first number:'))
    number_2=int(input('please type the second number:'))

    if operation=='+':
       print('{}+{}='.format(number_1,number_2))
       print(number_1+number_2)
     
    elif operation=='-':
       print('{}-{}='.format(number_1,number_2))
       print(number_1-number_2)

    elif operation=='*':
       print('{}*{}='.format(number_1,number_2))
       print(number_1*number_2)

    elif operation=='/':
       print('{}/{}='.format(number_1,number_2))
       print(number_1/number_2)

    else:
       print('you have operated wrongly, please try again')

calculation()