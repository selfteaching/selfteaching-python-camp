
operator=input('请输入运算符（+、—、*、/）:')#input 里面的字符串的作用是在等待输入的时候进行提示
first_number=input('请输入第一个数字:')
second_number=input('请输入第二个数字:')
a=int(first_number)#int(first_number)在这里的作用是把str类型的first_number转换成int类型
b=int(second_number)
print('operator:',operator,type(operator))
#print('first_number:',first_number,type(first_number),type(a)）
#print('second_number:',second_number,type(second_number),type(b)）
#print('测试加法str加法：'，frist_number+second_number)
#print('测试加法str减法：'，frist_number-second_number)
if operator=='+':
    print(a,'+',b,'=',a+b)
elif operator=='-':
    print(a,'-',b,'=',a-b)
elif operator=='*':
    print(a,'*',b,'=',a*b)
elif operator=='/':
    print(a,'/',b,'=',a/b)
else:
    print('无效的运算符')
    # raise ValueError('无效的运算符')