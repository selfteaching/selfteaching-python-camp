def add_numbers( ):
    a=input("Type the first number: ")
    b=input("Type the second number: ")
    a=float(a)
    b=float(b)
    c=a+b
    print("The result is ",c )

def sub_numbers( ):
    a=input("Type the first number: ")
    b=input("Type the second number: ")
    a=float(a)
    b=float(b)
    c=a-b
    print("The result is ",c )


def mul_numbers( ):
    a=input("Type the first number: ")
    b=input("Type the second number: ")
    a=float(a)
    b=float(b)
    c=a*b
    print("The result is ",c )

def div_numbers( ):
    a=input("Type the first number: ")
    b=input("Type the second number: ")
    a=float(a)
    b=float(b)
    c=a/b
    print("The result is ",c )

cal_type = input("If you want to add_numbers enter 1 ; If you want to sub_numbers enter 2;If you want to mul_numbers enter 3;If you want to div_numbers enter 4:")
cal_type = str(cal_type)

if  cal_type == "1":
    add_numbers( )
elif cal_type == "2":
    sub_numbers( )
elif cal_type == "3":
    mul_numbers( )
elif cal_type == "4":
    div_numbers()
