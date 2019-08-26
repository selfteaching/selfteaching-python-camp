import math
def add (x,y):
    return x+y 
def minus (x,y):
    return x-y
def mutiply (x,y):
    return x*y
def divide (x,y):
    return x/y
print ("""\
    please input your choice 
    add:1 
    minus:2 
    mutiply:3 
    divide:4
""")
choice=input ("please choose your calculator number:")
num1 =int(input("number1:"))
num2 =int(input("number2:"))
if choice=='1':
    print(num1,"+", num2, "=",add(num1,num2))
elif choice=='2':
        print(num1,'-',num2,'=', minus(num1,num2))
elif choice=='3':
        print(num1,'*',num2,'=',mutiply(num1,num2))
elif choice=='4':
        print(num1,'/',num2,'=',divide(num1,num2))
else:
    print("error")