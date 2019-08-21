# 计算器程序

Operator=input('请输入运算符号（+、-、*、/):')
first_number=input('请输入第一个数字：')
second_number=input('请输入第二个数字：')

a=int(first_number)
b=int(second_number)

if Operator=="+":
    print(a,'+',b,'=',a+b)
elif Operator=="-":
    print(a,'+',b,'=',a-b)
elif Operator=="*":
    print(a,'+',b,'=',a*b)
elif Operator=="/":
    print(a,'+',b,'=',a/b)
else:
    Print('无效的运算符号')