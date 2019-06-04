num1 = float(input('请输入数字：'))
num2 = float(input('请输入数字：'))
operator = input('请输入运算符：加法"+"，减法"-"，乘法"*"，除法"/": ')
if operator == '+':
   print(num1 + num2 )
elif operator == '-':
   print(num1 - num2 )
elif operator == '*':
   print(num1 * num2 )
elif operator == '/':
   if num2 == 0:
      print("输入错误，除数不能为0")
   else:
      print(num1 / num2 )
else:
   print('输入错误')
