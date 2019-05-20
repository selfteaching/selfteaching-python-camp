def add(x,y):
    return x + y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print('请输入数字开始计算')
a=int(input(''))
print('请选择运算方式：+,-,*,/')
b=input('')
print('请继续输入数字')
c = int(input(''))
if b == '+':
    print(add(a,c))
elif b == '-':
    print(substract(a,c))
elif b == '*':
    print(multiply(a,c))
elif b == '/':
    print(divide(a,c))
else:
    print('输入错误')