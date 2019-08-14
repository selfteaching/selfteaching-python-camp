operator=input('请输入运算符（+、-、*、/):')
a=int(first_number)
b=int(second_number)

print('operator:',operator,type(operator))
print('first_number:',type(first_number),type(a))
print('second_number,'type(second_number),type(b))

print('测试加法str加法:',first_number+second_number) 

if operator =='+':
    print(a,'+',b,'=',a+b)
elif operator=='-'：
    print(a,'-',b,'=',a-b)
elif operator=='*':
    print(a,'*',b,'='a*b)
elif operator=='/':
    print(a,'/',b,'=',a/b)
else:
    print('无效的运算')

#一定要在terminal 状态下运行程序，否则程序出错
