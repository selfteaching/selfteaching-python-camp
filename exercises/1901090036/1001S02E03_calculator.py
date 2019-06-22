def multiplication(a,b):
    return a*b
print("please input the first number:")
a=int(input(''))
print("please choose:+,-,*,/,")
c=input('')
print("please input the second number:")
b=int(input(''))
if c=="*":
    print(multiplication(a,b))
else:
    print("wrong message")