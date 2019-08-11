# 
# 这里是单行注释

''' 嘿嘿嘿
这是 （顶着开头这行开头写，开头与line2的#对齐）
多行注释
注释的作用：给人看，方便理解。不运行
'''

"""
这也是
多行注释
"""

# 计算器确定三个输入信息，分别是运算符、运算符左边的数字和运算符右边的数字

# The equal sign (=) is used to assign a value to a variable（给变量赋值）
# string(字符串) 是'' "" 里的东西
# 把内置函数 input 接收的输入字符 赋值 给变量
operator = input('请输入运算符（+、-、*、/）:') # input里面字符串的作用是在等待输入的时候进行提示
first_number = input('请输入第一个数字：')
second_number = input('请输入第二个数字：')

a = int(first_number) # int(first_number)在这里的作用：把str类型 的first_number 转换成 int 类型(a type of numbers)
b = int(second_number)

# The print() function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters
# print() 打印后 括号内，逗号分隔的部分之间无自动空格
print('operator:', operator, type(operator)) 
print('first_number:', first_number, type(first_number), type(a))
print('second_number:', second_number, type(second_number), type(b))

print('测试加法 str 加法：', first_number + second_number) # 与int类型的加法比较
# print('测试加法 str 减法：'，first_number - second_number) # 错误。字符串不支持减法运算


if operator == '+': # == 值相等
    print(a, '+', b, '=',a + b) #缩进：默认4空格。按tab/空格键4次
elif operator == '-':
    print(a, '-' ,b,'=' ,a - b)
elif operator == '*':
    print(a, '*', b, '=', a * b)
elif operator == '/':
    print(a, '/', b, '=',a/b) # 运算符号前后无空格不影响～逗号后有空格也不影响～
else:
    print('无效运算符')
    # raise ValueError(无效运算符)