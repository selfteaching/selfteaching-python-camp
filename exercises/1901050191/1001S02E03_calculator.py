def calculator():
    d = input('输入第一个数字')
    e = input('输入第二个数字')
    c = input('请输入计算符号(+, -, *, /) : ')
    a = int(d)
    b = int(e)
    print(a)
    print(b)
    print(c)
    if c == '+':
        print(a, '+', b, '=', a + b )
    if c == '-':
        print(a, '-', b, '=', a - b )
    if c == '*':
        print(a, '*', b, '=', a * b )
    if c == '/':
        print(a, '/', b, '=', a / b )
    
calculator()