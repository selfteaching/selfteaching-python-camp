# 计算器

operator = input('请输入运算符（+、-、*、/）:') # input 里面的字符串的作用是在等待输入的时候进行提示
first_number = input('请输入第一个字数')
second_number = input('请输入第二个字数')

a = int(first_number) # int(first_number) 在这里的作用是把 str 类型的 first_number 转换成 int 类型
b = int(second_number)

print('operator:',operator,type(operator))
print('first_number:', type(first_number),type(a))
print('second_unmber:',type(second_number),type(b))

# print('测试加法 str 法：', first_number + second_number)
# print('测试减法 str 减法：', first_number - second_number)

if operator == '+':
    print(a, "+", b, '=', a+b)
elif operator == '-':
    print(a, '-', b, '=', a-b)
elif operator == '*':
    print(a, '*', b, '=', a*b)
elif operator == '/' :
    print(a, '/', b, '=', a/b)
else:
    print('无效运算符') # raise ValueError('无效的运算符')