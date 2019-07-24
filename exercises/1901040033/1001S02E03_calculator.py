def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

print("choose operator：")
print("1.add")
print("2.sub")
print("3.multi")
print("4.div")

choice = input("input ur choice(1/2/3/4):")

num1 = int(input("input 1st number: "))
num2 = int(input("input 2nd number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("invaild input")