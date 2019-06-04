num1 = int(input("输入第一个数字: "))
print("输入运算符：")
print("'+'、相加")
print("'-'、相减")
print("'*'、相乘")
print("'/'、相除")
choice = input("输入你的选择(+|-|*|/):")
num2 = int(input("输入第二个数字: "))
 
if choice == '+':
   print(num1,"+",num2,"=", num1+num2)
 
elif choice == '-':
   print(num1,"-",num2,"=", num1-num2)
 
elif choice == '*':
   print(num1,"*",num2,"=", num1*num2)
 
elif choice == '/':
   print(num1,"/",num2,"=", num1/num2)
else:
   print("非法输入")
