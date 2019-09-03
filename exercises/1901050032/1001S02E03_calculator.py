#define the function
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y  
#operation of users 
print('+')
print('-')
print('*')
print('/')
num1 = int(input('please enter the number:'))
choice = input('please enter the operational symbol')
num2 = int(input('please enter the number:'))
if choice == '+':
   print(num1, '+', num2, '=', add(num1, num2))
elif choice == '-':
    print(num1, '-', num2, '=', subtract(num1, num2))
elif choice == '*':
    print(num1, '*', num2, '=', multiply(num1, num2))
elif choice == '/':
    print(num1, '/', num2, '=', divide(num1, num2))
else:
    print('please enter the valid operational symbol again')
