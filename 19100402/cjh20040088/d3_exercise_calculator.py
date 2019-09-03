def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiple(x,y):
    return x*y
def divide(x,y):
    return x/y

print("choice:")
print("1.add")
print("2.subtract")
print("3.multiple")
print("4.divide")

choice=input("input the choice(1/2/3/4):")

num1 = int(input("type the num1:"))
num2 = int(input("type the num2:"))

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))

elif choice=='2':
    print(num1,"-",num2,"=",subtract(num1,num2))

elif choice=='3':
    print(num1,"*",num2,"=",multiple(num1,num2))

elif choice=='4':
    
    if num2==0:
        print("Invalid input")
    else:
        print(num1,"/",num2,"=",divide(num1,num2))

else:
    print("Invalid input")
