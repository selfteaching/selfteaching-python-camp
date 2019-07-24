operator = input('Please input the operator you want to do:\n')

if operator != '+' and operator != '-' and operator != '*' and operator != '/':

    print("\nThe operator you input is not '+' '-' '*' '/'!!!")
        
    operator = input('Please input the operator you want to do again:\n')

if operator == '+':

    a = input('\nPlease input the first number: ')
    
    b = input('Please input the second number: ')

    result = float(a) + float(b)
    
    print(a,operator,b,'=',result)

if operator == '-':

    a = input('\nPlease input the first number: ')
    
    b = input('Please input the second number: ')

    result = float(a) - float(b)

    print(a,operator,b,'=',result)

if operator == '*':

    a = input('\nPlease input the first number: ')
    
    b = input('Please input the second number: ')

    result = float(a) * float(b)

    print(a,operator,b,'=',result)

if operator == '/':

    a = input('\nPlease input the first number: ')
    
    b = input('Please input the second number: ')

    result = float(a) / float(b)
    
    print(a,operator,b,'=',result)

