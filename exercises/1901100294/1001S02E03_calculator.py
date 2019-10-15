want = input('你想进行什么计算？（加、减、乘或除）')
if want == '加':
    a = int(input('请输入一个加数:'))
    b = int(input('请输入另一个加数:'))
    c = a + b
    print('{} + {} = {}'.format(a,b,c))
elif want == '减':
    a = int(input('请输入一个减数:'))
    b = int(input('请输入另一个减数：'))
    c = a - b
    print('{} - {} = {}'.format(a,b,c))
elif want == '乘':
    a = int(input('请输入一个乘数：'))
    b = int(input('请输入另一个乘数：'))
    c = a * b
    print('{} + {} = {}'.format(a,b,c))
elif want == '除':
    a = int(input('请输入一个除数：'))
    b = int(input('请输入另一个除数'))
    c = a / b
    print('{} / {} = {}'.format(a,b,c))