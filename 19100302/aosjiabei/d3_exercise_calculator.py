#支持加减乘除的计算器，支持输入参数和输出结果
print("hi,i am a caculator,provide two numbers ")
i=int(input("please,give me the first number:"))
operator=input("enter the type of calculation， + or - or * or / :")
j=int(input("please,give me th second number："))

if operator=="+"or operator== "-"or operator=="*"or operator=="/":
    if operator == "+":
        print(i+j)
    if operator == "-":
        print(i-j)
    if operator =="*":
        print(i*j)
    if operator == "/":
        print(i/j)
else:
    print ("please enter + or - or * or /")
