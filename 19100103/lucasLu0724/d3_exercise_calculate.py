print("helloworld")

def cal():
    print("welcome")
    num1=float(input("please input the num1"))
    num2=float(input("please input the num2"))
    option =input("please input the option :+ - * /")

    if option=="+":
        print("{0}+{1}=".format(num1,num2),num1+num2)
    elif option=="-":
        print("{0}-{1}=".format(num1,num2),num1-num2)
    elif option=="*":
        print("{0}*{1}=".format(num1,num2),num1*num2)
    elif option=="/":
        print("{0}/{1}=".format(num1,num2),num1/num2)
    else:
        print("vaild operation!")

cal()
