while True:
    number1 = input("Enter a number1:\n")
    number2 = input("Enter a number2:\n")
    operator = input("Please choose: + or - or * or /\n")
    if operator=="/" and number2 == "0":
            print("number2 can NOT be 0")
    else:
        break

if operator=="+":
    print("Answer:\n",number1,"+",number2,"=",float(number1)+float(number2))
if operator=="-":
    print("Answer:\n",number1,"-",number2,"=",float(number1)-float(number2))
if operator=="*":
    print("Answer:\n",number1,"*",number2,"=",float(number1)*float(number2))

if operator=="/":
    print("Answer:\n",number1,"/",number2,"=",float(number1)/float(number2))