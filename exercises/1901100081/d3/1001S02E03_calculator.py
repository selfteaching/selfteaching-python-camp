operator=input('请输入运算符（+、-、*、/）：')
first_number=input('请输入第一个数字')
second_number=input('请输入第二个数字')

a=int(first_number)
b=int(second_number)

if operator =='+':
    print(a,'+',b,'=',a+b)
elif operator =='-':
    print(a,'-',b,'=',a-b)
elif operator == '*':
    print(a,'*',b,'=',a*b)
elif operator =='/':
    print(a,'/',b,'=',a/b)
else:
    print('无效的运算符')