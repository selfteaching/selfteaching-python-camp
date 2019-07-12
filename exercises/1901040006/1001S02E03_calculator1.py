def calculator():
    num_1 = int(input('请输入要计算的第一个数字：'))
    symbol = input(('请输入一个运算符，+ - * /：'))
    num_2 = int(input('请输入要计算的第二个数字：'))
    if symbol == '+':
        result = num_1 + num_2
    elif symbol == '-':
        result = num_1 - num_2
    elif symbol == '*':
        result = num_1 * num_2
    elif symbol == '/':
        result = num_1 / num_2
    print(result)