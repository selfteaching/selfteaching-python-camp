operator = input('请输入运算符（+,-,*,/,^）:')
first_num = input('请输入第一个数 : ')
second_num = input('请输入第二个数 : ')

a=int(first_num)
b=int(second_num)

print('operator',operator,type(operator))
print('first_num:',first_num,type(first_num),type(a))
print('second_num:',second_num,type(second_num),type(b))

print('测试加法 str 加法',first_num+second_num)
#print('测试减法 str 减法',first_num-second_num)

if operator=='+':
    print(a,'+',b,'=',a+b)
elif operator=='-':
    print(a,'-',b,'=',a-b)
elif operator=='*':
    print(a,'*',b,'=',a*b)
elif operator=='/':
    print(a,'/',b,'=',a/b)
elif operator=='^':
    print(a,'^',b,'=',a**b)
else:
    print('无效运算符')