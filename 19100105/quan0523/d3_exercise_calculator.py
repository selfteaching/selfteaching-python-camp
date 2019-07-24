def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y 

def subtract(x, y): 
    print("x is {} and y is {}".format(x, y))
    return x - y 

def multiply(x, y):
    print("x is {} and y is {}".format(x, y))
    return x * y 

def divide(x, y):
    print("x is {} and y is {}".format(x, y))
    return x / y 

print（“operat：”）
print（“1、add”）
print（“2、subtract”）
print（“3、multiply”）
print（“4、divide”）

choice = input("enter your choice(1/2/3/4):")

num1 = int(input("type first number:"))
num2 = int(input("type secend number:"))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))
    
elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))

else:
    print("Error")