
operator = input ('请输入参数值（+，-，*，/，//，%）：')
first_number = input('请输入第一位数字：')
second_number = input('请输入第二位数字：')

a = int(second_number)
b = int(first_number)

if operator == "+":
    print (a , '+' , b , "=" , a+b )
elif operator == "-":
    print (a,'-',b,'=',a-b)
elif operator == '*':
    print (a,'*',b,'=',a*b)
elif operator == '/':
    print (a,'/',b,'=',a / b )
else:
    print ('操作符无效')