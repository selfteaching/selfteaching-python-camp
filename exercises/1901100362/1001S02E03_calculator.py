while True:
    print("""请选择运算符:
        1. +
        2. -
        3. *
        4. /""")
    sign = input()

    x = eval(input('请输入第一个数：'))
    y = eval(input('请输入第二个数：'))
    print()

    if sign == '1':
        result = x + y
        print(f'{x} + {y}= {result}\n')
    elif sign == '2':
        result = x - y
        print(f'{x} - {y}= {result}\n')
    elif sign == '3':
        result = x * y
        print(f'{x} * {y}= {result}\n')
    elif sign == '4':
        if y == 0:
            print('除数不能为0!\n')
            continue
        result = x / y
        print(f'{x} / {y}= {result}\n')
    else:
        print("退出程序")
        break




