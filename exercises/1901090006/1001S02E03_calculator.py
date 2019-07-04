def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("please input the number to calculate")
x=int(input(''))
print('please choose：+，-，*，/')
z=input('')
print('please continue to input the number')
y=int(input(''))

if z == "+":
    print(add(x,y))
elif z == "-":
    print(subtract(x,y))
elif z == "*":
    print(multiply(x,y))
elif z == "/":
    print(divide(x,y))
else: 
    print("The string you input is error.")