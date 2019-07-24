def cal():
    print('我的个人计算器')
    numA = float(input('请输入第一个数字: '))
    op = input('请选择一种运算(+-*/): ')
    if op=='+':
        numB = float(input('请输入第二个数字: '))
        print ("结果为 ",numA+numB)
    elif op == '-':
        numB = float(input('请输入第二个数字: '))
        print( "结果为 ",numA-numB)
    elif op == '*':
        numB = float(input('请输入第二个数字: '))
        print ("结果为 ",numA*numB)
    elif op == '/':
        numB = float(input('请输入第二个数字: '))
        print ("结果为",numA/numB)

cal()