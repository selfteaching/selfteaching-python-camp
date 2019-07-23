# 这是单行注释
# 计算器确定3个输入值，分别是运算符、运算符左边的数字和右边的数定
# 把内置函数input 接收的 输入字符 赋值 给 变量
operator = input('请输入运算符(+、-、*、/):')
first_number = input('请输入第一个数字:')
second_number = input('请输入第二个数字:')

a = int(first_number)
b = int(second_number)

print('operator',operator,type(operator))
print('first_number',first_number,type(first_number),type(a))
print('second_number',second_number,type(second_number),type(b))

print('测试',operator,'法:',first_number,operator,second_number)

if operator == '+':
    print(a,'+',b,'=',a + b)
elif operator == '-':
    print(a,'-',b,'=',a - b)
elif operator == '*':
    print(a,'*',b,'=',a * b)
elif operator == '/':
    print(a,'/',b,'=',a / b)
else:
    print('无效的运算符')