<<<<<<< HEAD
def cool(x,y):
    return (x*y)
print("赶紧输入第一个数字:")
a=int(input(''))
print('请选择：+，-，*，/')
c=input('')
print('请输入第二个数字:')
b=int(input(''))
if c=='*':
    print(cool(a,b))
else:
    print("请重新输入")
    
    
=======
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
>>>>>>> d3a2e58026ae54f2ca999d5c37f1f4db333a115f
