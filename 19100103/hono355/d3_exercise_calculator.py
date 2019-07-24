def cal():
    numA = float(input('请输入第一个数字：'))
    numB = float(input('请输入第二个数字：'))
    op = input('请选择一个操作(+-*/)：')
    if op == '+':
        print('结果为：', numA + numB)
    elif op == '-':
        print('结果为：', numA - numB)
    elif op == '*':
        print('结果为：', numA * numB)
    elif op == '/':
        print('结果为：', numA / numB)
    else:
        print('无效', op)


cal()
