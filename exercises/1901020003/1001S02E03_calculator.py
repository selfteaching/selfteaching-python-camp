# 计算器的三个输入值，分别是运算符左边数字、运算符、运算符右边输入数字

# 把内置函数 input 接收的 输入字符 赋值 给 变量
operator = input(‘请输入运算符（+、-、*、/、)： ’）# input中字符串的作用是等待输入的时候进行的提示
first_number = input(‘请输入第一个字符: ’)
second_number = input(‘请输入第二个字符: ’)

a = int(first_number) # int(first_number) 在这里的作用是 把 str 类型 的 first_number 转换成 int 类型的
b = int(second_number)

print(‘operator:’, operator, type(operator))
print(‘first_number:’, first_number, type(first_number))
print(‘（second_number:’, second_number, type(second_number))

print(‘测试加法 str 加法:’， first_number + second_number)
print(‘测试减法’ str 减法:’， first_number - second_number )

if operator == ‘+’ :
    print（a, ‘+’, b, a+b)
elif operator == ‘-’ :
    print（a, ‘-’, b, a-b)
elif operator == ‘*’ :
    print（a, ‘*’, b, a*b)
elif operator == ‘/’ :
    print（a, ‘/’, b, a/b)
else:
    print（‘打印无效运算符’）
    # ralse ValuErroer(‘无效运算符’)