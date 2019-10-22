def calculate(operate,a,b):

    if operate=="+":
        print(a +b )
    elif operate=="-":
        print(a -b )
    elif operate=="*":
        print(a *b )
    elif operate=="/":
        print(a /b )
    else:
        print("invalid input,please try+-*/")

a =int(input("please input your number:")) 
operate=input("please input the sign of operation:")
b =int(input("please input your number:")) 
#use the above defined function to calculate
calculate(operate,a,b)