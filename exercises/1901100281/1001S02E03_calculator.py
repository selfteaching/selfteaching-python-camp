operator = input("please enter an operator('+', '-', '*', '/')")
num1 = float(input("please enter the first number"))
num2 = float(input("please enter the second number"))

if operator == '+':
    print(num1, '+', num2, '=', float(num1+num2))
elif operator == '-':
    print(num1, '-', num2, '=', float(num1-num2))
elif operator == '*':
    print(num1, '*', num2, '=', float(num1*num2))
elif operator == '/':
    if num2 ==0:
        print("error enter, ZeroDivisionError")
    else:
        print(num1, '/', num2, '=', float(num1/num2))
else:
    print("error enter")