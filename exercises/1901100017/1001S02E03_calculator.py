# calculator
# filename 1001S02E03_calculator.py
firstchoice = 1
calculatchoice = 0
while firstchoice == 1:
    print("this is a calculator program   1. use calculator  2. end")
    firstchoice = int(input("what is your choice     "))
    if firstchoice == 1:
        print("I can do 1. plus 2. minus 3. multiply 4. divide")
        calculatchoice = int(input("which calculation would you like      "))
        number1 = float(input("please enter the first number   "))
        number2 = float(input("please enter the second number   "))
        if calculatchoice == 1:
            result = number1 + number2
        elif calculatchoice == 2:
            result = number1 - number2
        elif calculatchoice == 3:
            result = number1 * number2
        else:
            result = number1 / number2
        print("result is ", result)


else:
    print("goodbye!")

