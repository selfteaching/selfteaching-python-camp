def cal():
    numA = float(input('请输入一个数字: '))
    op = input('请选择一个操作(+-*/):')
    #numB = float(input('请输入另一个数字:'))
    if op == '+':
        numB = float(input('请输入另一个数字'))
        print("结果：",numA+numB)
    elif op == '-':
        numB = float(input('请输入另一个数字'))
        print("结果：",numA-numB)
    elif op == '*':
        numB = float(input('请输入另一个数字'))
        print("结果：",numA*numB)
    elif op == '/':
        numB = float(input('请输入另一个数字'))
        print("结果：",numA/numB)
    else:
        print("无效操作",op)

cal()