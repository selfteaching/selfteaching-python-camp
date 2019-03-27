def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("Welcome to use the calculator!")
print("Please choose the type of calculation")
print("+(1)  -(2)  *(3)  /(4)")
choice=input()
num1=int(input("The first num is:"))
num2=int(input("The second num is:"))
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))
    
elif choice == '2':
    print(num1,"-",num2,"=", sub(num1,num2))
    
elif choice == '3':
    print(num1,"*",num2,"=", mul(num1,num2))
    
elif choice == '4':
    print(num1,"/",num2,"=", div(num1,num2))

else:
    print("The choice is invalid")
