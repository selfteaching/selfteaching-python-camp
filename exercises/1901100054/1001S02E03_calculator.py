# 计算器确定三个输入值，分别是运算符，及其左右的数字

# 把内置函授 inter 接收的输入字符赋值给变量
operator = input('sr（+、-、*、/) : ') # input 里面的字符串的作用是在等待输入的时候进行提示
first_number = input('first：')
second_number = input('second：')

a = int(first_number) # int(first_number) 在这里的作用是把 str 类型的 first_number 转换成 int 类型
b = int(second_number)

print('operator:',operator, type(operator))
print('first_number:',first_number, type(first_number), type(a))
print('second_number:',second_number, type(second_number), type(b))


if operator == '+' :
    print(a,'+', b , '=', a + b)
elif operator == '-':
    print(a, '-', b , '=', a - b)
elif operator == '*':
    print(a, '*', b , '*', a * b)
elif operator == '/':
    print(a, '/', b , '=', a / b)
else:
    print('invalid')