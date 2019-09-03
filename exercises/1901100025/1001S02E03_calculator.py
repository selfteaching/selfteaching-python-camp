cal = int(input("What kind of calculation? \n1 is '+',\n2 is '-',\n3 is '*',\n4 is '/' \n(Please enter the number):  "))
a = float(input("Please enter an integer: "))
b = float(input("please enter another interger: "))

if cal == 1:
    print(a+b)
elif cal == 2:
    print(a-b)
elif cal == 3:
    print(a*b)
elif cal == 4:
    print(a/b)