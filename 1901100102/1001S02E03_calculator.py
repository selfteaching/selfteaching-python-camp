
# 这是单行注释

'''
这是
多行注释
注释的作用只是方便我们理解代码，并不参与执行
'''

"""
这也是
多行注释
"""

# 计算器确定输入三个值，分别是运算值，运算符左边的数字和运算符右边的数字

# 把内置函数 input 接收的 输入字符 赋值 给 变量
operator = input('请输入运算符（+、-、*、/）：')# input 里面的字符串的作用是在等待输入的时候进行提示
first_number = input('请输入第一个数字：')
second_number = input('请输入第二个数字：')

a = int(first_number) # int(first_number) 在这里的作用是 把 str 类型 的 first_number 转换成 int 类型
b = int(second_number)

print('operator:',operator,type(operator) )
print('firsr_number:',first_number,type(first_number),type(a))
print('second_number:',second_number,type(second_number),type(b))

print('测试加法 str 加法：',first_number + second_number)
# print(测试加法 str 减法：', first_number - second_number)


if operator == '+':
    print(a, '+', b, '=', a + b)
elif operator == '-':
    print(a, '-', b, '=', a - b)
elif operator == '*':
     print(a, '*', b, '=', a * b)
elif operator == '/':
    print(a, '/', b, '=', a / b)
else:
    print('无效的运算符')
    # raise ValueError('无效的运算符')
