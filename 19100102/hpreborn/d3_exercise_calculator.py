#mycalculator
def mycalculator():
    num1 = input("please type the first number:")
    calculate_sigh = input("please type one of the following calculation type:+ or - or * or /:")
    num2 = input("please type the second number:")
    num1 = int(num1)
    calculate_sigh = str(calculate_sigh)
    num2 = int(num2)
    if calculate_sigh == "+":
        result = num1 + num2
    elif calculate_sigh == "-":
        result = num1 - num2
    elif calculate_sigh == "*":
        result = num1 * num2
    elif calculate_sigh == "/":
        result = num1 / num2
    else:
        result = "error"
    print(num1,calculate_sigh,num2,"=",result)
mycalculator()