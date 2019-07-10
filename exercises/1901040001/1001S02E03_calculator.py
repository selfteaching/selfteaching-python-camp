# using Python to make a simple calculator

def add(a,b):            #add two number
    return a + b

def subtract(c,d):       #subtract two number
    return c - d

def multiply(e,f):       #multiply two number
    return e * f

def divide(g,h):         #divide two number
    return g / h

#choose the operation of two number
print('1.add')
print('2.subtrcat')
print('3.multiply')
print('4.divide')
operation = input('choose the operation(1/2/3/4):')
num1 = int(input('enter the first number:'))
num2 = int(input('enter the second number:'))

if operation == '1':
    print('num1','+','num2','=',add(num1,num2))
elif operation == '2':
    print('num1','-','num2','=',subtract(num1,num2))
elif operation == '3':
    print('num1','*','num2','=',multiply(num1,num2))
elif operation == '4':
    print('num1','/','num2','=',divide(num1,num2))
else:
    print('please type the serial number correctly')