# This is my calculator with python language

print('A calculator with python language')
operator=input('Please enter an operator (+, -, *, /) : ')
first_number=input('Please enter the first number : ')
second_number=input('Please enter the second number : ')

a=int(first_number)#定义a等于第一个数字（数值型）
b=int(second_number)#定义b等于第二个数字（数值型）

if operator=='+':#如果输入+
    print(a, '+', b, '=', a + b)#显示两个数字相加及结果
elif operator=='-':#如果输入-
    print(a, '-', b, '=', a - b)#显示两个数字相减及结果
elif operator=='*':
    print(a, '*', b, '=', a * b)  
elif operator=='/':
    print(a, '/', b, '=', a / b)
else:
    print('Null operator') #其他情况，显示无效输入        