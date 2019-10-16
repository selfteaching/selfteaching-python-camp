##wlecome to Calculator
##1.接收用户输入的运算符号和数字
symbol = input ('请输入+，-，*，/中的运算符号')
num1 = input('请输入第一个数字')
num2 = input('请输入第二个数字')

##2.把用户输入的数字（字符串）转换成整形
a = int(num1)
b = int(num2)

##3.计算

if symbol == '+':
    print (a,'+',b,'=', a+b)
elif symbol == '-':
    print (a,'-',b,'=', a-b)
elif symbol == '*':
    print (a,'*',b,'=', a*b)
elif symbol == '/':
    print (a,'/',b,'=', a/b)
else:
    print('非法输入')