def calculate():
    formula = input('''\
    Easy Calculator
    请输入公式+、-、*、/：
''')
    number_1 = float(input('请输入数字：'))
    number_2 = float(input('请输入数字：'))
    if formula == str('+'):
            print(number_1+number_2)
    elif formula == str('-'):
            print(number_1-number_2)
    elif formula == str('*'):
            print(number_1*number_2)
    elif formula == str('/'):
            print(number_1/number_2)
    else: 
            print("please enter 1the right formula")
            return calculate()
    
        # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N fosr NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()
calculate() 
