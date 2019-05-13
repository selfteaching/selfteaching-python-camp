def calculate(operate,numA,numB):

    if operate=="+":
        print(numA+numB)
    elif operate=="-":
        print(numA-numB)
    elif operate=="*":
        print(numA*numB)
    elif operate=="/":
        print(numA/numB)
    else:
        print("invalid input,please try+-*/")

operate=input("please input the sign of operation:")
numA=int(input("please input your number:"))
numB=int(input("plaese input your number:"))

#use the above defined function to calculate
calculate(operate,numA,numB)