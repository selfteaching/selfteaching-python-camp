operator = input('请输入运算符："+"，"-"，"*"，"/": ')
num1 = float(input('请输入第一个数字：'))   #input输入，让用户输入一些值，，并将其赋给num1
num2 = float(input('请输入第二个数字：'))   #float()作为一个内建函数，将输入的值转换为浮点数格式

if operator == '+':                      #if...  elif...语句的流程控制
   print(num1,"+",num2,"=",float((num1 + num2)) )
elif operator == '-':
   print(num1,"-",num2,"=",float((num1 - num2)) )
elif operator == '*':
   print(num1,"*",num2,"=",float((num1 * num2)) )
elif operator == '/':
   if num2 == 0:                         
      print("输入错误，除数不能为0")
   else:
      print(num1,"/",num2,"=",float((num1 / num2)) )
else:
   print('输入错误')