while True:
    a = input('按例子输入进行计算(eg:1 + 1 或 1 - 1 或 1 * 1 或 1 / 1) 或 按quit退出计算：\n')
    a = a.strip()
    if a == 'quit':
        break
    elif '*' in a:
        b = a.partition('*')
        c = float(b[0]) * float(b[2])
        print('{0} = {1}'.format(a,c))
    elif '/' in a:
        b = a.partition('/')
        c = float(b[0]) / float(b[2])
        print('{0} = {1}'.format(a,c))
    else:
        for i in a[1:]:
            if i == '+':
                b = a.partition(i)
                c = float(b[0]) + float(b[2])
                print('{0} = {1}'.format(a,c))
                break
            elif i == '-':
                b = a.partition(i)
                c = float(b[0]) - float(b[2])
                print('{0} = {1}'.format(a,c))
                break