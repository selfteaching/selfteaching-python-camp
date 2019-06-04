# 将字符转换为运算
import operator
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

# 输入数字及运算符
number_1 = int(input('Enter your first number: '))

operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_2 = int(input('Enter your second number: '))

# 输出计算结果
print('{} {} {} = {}'.format(number_1, operation, number_2, ops[operation](number_1, number_2)))