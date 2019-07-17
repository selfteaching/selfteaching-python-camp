# 计算器
i = 2
while i>1:
    # 输入，选择想要进行的运算
    print('选择想要进行的运算：')
    print('1 代表“相加”')
    print('2 代表“相减”')
    print('3 代表“相乘”')
    print('4 代表“相除”')
    choice = input('输入你想进行的运算(1/2/3/4):')
    # 输出运算结果
    if choice == '1':
        num1 = int(input('输入第一个数: '))
        num2 = int(input('输入第二个数: '))
        print('运算结果：',num1,'+',num2,'=', num1+num2)
    elif choice == '2':
        num1 = int(input('输入第一个数: '))
        num2 = int(input('输入第二个数: '))
        print('运算结果：',num1,'-',num2,'=', num1-num2)
    elif choice == '3':
        num1 = int(input('输入第一个数: '))
        num2 = int(input('输入第二个数: '))
        print('运算结果：',num1,'×',num2,'=', num1*num2)
    elif choice == '4':
        num1 = int(input('输入第一个数: '))
        num2 = int(input('输入第二个数: '))
        print('运算结果：',num1,'÷',num2,'=', num1/num2)
    else:
        print('非法输入！请重新输入')
    print('\n')