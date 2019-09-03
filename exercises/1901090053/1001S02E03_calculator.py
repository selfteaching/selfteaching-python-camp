def calculator():
    num1 = float( input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    operator = input("Enter an operator: ")
    if operator == '+':
        result = num1 + num2
        print (num1, ' + ', num2, ' = ', result)
    if operator == '-':
        result = num1 - num2
        print (num1, ' - ', num2, ' = ', result)
    if operator == '*':
        result = num1 * num2
        print (num1, ' * ', num2, ' = ', result)
    if operator == '/':
        result = num1 / num2
        print (num1, ' / ', num2, ' = ', result)

calculator ()
