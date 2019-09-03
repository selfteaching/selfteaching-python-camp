#简易计算器
#第一步：定义变量:运算符，左边数字，右边数字。
num1=input('请输入第一个数字：')
operator=input('请输入运算方式(+、-、*、/：')
num2=input('请输入第二个数字：')
a=int(num1)
b=int(num2)
if operator=='+':
    print(a,'+',b,'=',a+b)
elif operator=='-':
    print(a,'-',b,'=',a-b)
elif operator=='*':
    print(a,'-',b,'=',a*b)
elif operator=='/':
    print(a,'-',b,'=',a/b)
else:
    print('无效的运算符')

