def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    return x/y
operator = input('请选择运算符（+、-、*、/）：')
firster_number = input("请输入数字")
second_number = input("请输入另一个数字")

x = int (firster_number)
y = int (second_number)
print('operator:',operator,type(operator))
print('firster_number:',firster_number,type(firster_number),type(x))
print('second_number:',second_number,type(second_number),type(y))

if operator == '+':
    print(x,'+',y, '=', x+y)
elif operator == '-':
    print(x,'-',y, '=', x-y)
elif operator == '*':
    print(x,'*',y, '=', x*y)
elif operator == '/':
    print(x,'/',y, '=', x/y)
else:
    print("无效运算符")
