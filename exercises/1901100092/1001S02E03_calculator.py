a=float(input('请输入第一个数值:'))
operator=input('请输入运算符号(+,-,*,/):')
b=float(input('请输入第二个数值：'))
if operator=='+':
    print(a+b)
elif operator=='-':
    print(a-b)
elif operator=='*':
    print(a*b)
elif operator=='/':
    print(a/b)
else:
    print('无效的运算符')