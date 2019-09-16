operator = input('请输入运算符(+、-、*、/）：')
first_number = input('请输入第一个数字：')
second_number = input('请输入第二个数字：')

a = int(first_number)
b = int(second_number)

print('operator:',operator,type(operator))
print('first_number:',first_number,type(first_number),type(a))
print('second_number:',type(second_number),type(b))

print('测试加法 str 加法:',first_number + second_number)
# print('测试加法 str 减法:',first_number - second_number)

if operator == '+':
    print(a,'+',b,'=',a + b)
elif operator == '-':
    print(a,'-',b,'=',a - b)
elif operator == "*":
    print(a,'*',b,'=',a * b)
elif operator == "/":
    print(a,"/",b,'=',a / b)
else:
    print('无效的运算符')
    # raise valueerror('无效运算符)