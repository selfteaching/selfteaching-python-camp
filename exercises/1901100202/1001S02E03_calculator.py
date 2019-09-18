"""
实现一个简单的计算器
1 接收用户输入的第一个数字
2 接受用户输入的运算符
3 接受用户输入的第二个数字
4 代码进行判断，计算
5 显示计算的结果
"""
while True:
    # 实现一个简单的计算器
    # 1 接收用户输入的第一个数字
    first_num = input("请输入第一个数字:")
    first_num = int(first_num)
    # 2 接受用户输入的运算符
    symbol = input ("请输入运算符（+,-,*,/）:")
    # 3 接受用户输入的第二个数字
    second_num = input ("请输入第二个数字:")
    second_num = int(second_num)
    # 4 代码进行判断，计算
    # 4.1 如果运算符为+，进行加法运算
    if symbol == "+":
        result = first_num + second_num
        print(f'{first_num} {symbol} {second_num} = {result}')
        # print(result)
    # 4.2 如果运算符为-，进行减法运算
    elif symbol == "-":
        result = first_num - second_num
        print(f'{first_num} {symbol} {second_num} = {result}')
        # print(result)
    # 4.3 如果运算符为*，进行乘法运算
    elif symbol == "*":
        result = first_num * second_num
        print(f'{first_num} {symbol} {second_num} = {result}')
        # print(result)
    # 4.4 如果运算符为/，进行除法运算
    elif symbol == "/":
        if second_num == 0:
            result = "除数不能等于0"
            print(result)
        else:
            result = first_num / second_num
            print(f'{first_num} {symbol} {second_num} = {result}')
        # print(result)
    # 4.5 如果输入的符号不正确，提示错误
    else:
        result = "输入错误"
        print(result)
    # 5 显示计算的结果 显示出完整的格式，eg:1 + 1 = 2
        # 格式化输出 format
    # print(result)
    # print(f'{first_num} {symbol} {second_num} = {result}')


