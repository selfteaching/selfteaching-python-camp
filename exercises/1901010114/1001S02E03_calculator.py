def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print('请输入变量a的值')
a = int(input(''))
print('请选择+,-,*,/')
c = input('')
print('请输入变量b的值')
b = int(input(''))
if c == '+':
    print(add(a,b))
elif c == '-':
    print(subtract(a, b))
elif c == '*':
    print(multiply(a, b))
elif c == '/':
    print(divide(a, b))
else:
    print('输入错误') 

    