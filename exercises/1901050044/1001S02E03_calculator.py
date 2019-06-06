num1 = float(input('请输入数字：'))
num2 = float(input('请输入数字：'))
def add(x, y):
   return x + y 
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def devide(x, y):
   return x / y
print('请输入需要的运算法则')
print('1. 加法')
print('2. 减法')
print('3. 乘法')
print('4. 除法')
choice = input('请选择1/2/3/4：')
if choice == '1':
   print(num1 + num2 )
elif choice == '2':
   print(num1 - num2 )
elif choice == '3':
   print(num1 * num2 )
elif choice == '4':
   print(num1 / num2 )
else:
   print('输入错误')