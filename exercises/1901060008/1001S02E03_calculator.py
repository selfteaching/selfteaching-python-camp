while True:
    num1=float(input(''))
    operator=input('please enter +、-、*、/、**、%：')
    num2=float(input(''))
    if operator == '+':
        print(num1+num2)
    if operator == '-':
        print(num1-num2)
    if operator == '*':
        print(num1*num2)
    if operator == '/':
        print(num1/num2)
    if operator == '**':
        print(num1**num2)
    if operator == '%':
        print(num1%num2)