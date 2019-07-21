# day3作业，计算器
# 2019年7月4日
# 陈浩 

# 计算器确定3个输入值，运算符、第1数字、第2数字

# 把内置函数input 接收的数值交给变量
operator = input('请输入运算符（+、-、*、/）：')
first_number = input('请输入第一个数字：')
second_number = input('请输入第二个数字：')

a = int(first_number)
b = int(second_number)

print('operator:',operator,type(operator))
print('first_number:',first_number,type(first_number),type(a))
print('second_number:',second_number,type(second_number),type(b))

if operator == '+' :
    print('a+b','=',a + b)
elif operator == '-' :
    print('a-b','=',a - b)
elif operator == '*' :
    print('a*b','=',a * b)
elif operator == '/' :
       print('a/b','=',a / b)
else:
    print('无效的运算符')
