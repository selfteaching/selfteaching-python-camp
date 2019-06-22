def multiplication(a,b):
    return a*b
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def divide(a,b):
    return a/b
print("please input the first number:")
a=int(input(''))
print("please choose:+,-,*,/,")
c=input('')
print("please input the second number:")
b=int(input(''))
if c=="*":
    print(multiplication(a,b))
elif c=="+":
    print(add(a,b))
elif c=="-":
    print(substract(a,b))
elif c=="/":
    print(divide(a,b))
else:
    print("wrong message")