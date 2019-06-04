def add(x, y):
 
   return x + y
 
def subtract(x, y):
 
   return x - y
 
def multiply(x, y):
 
   return x * y
 
def divide(x, y):
 
   return x / y
 
print("请选择算法：")
print("1、加")
print("2、减")
print("3、乘")
print("4、除")

print("请选择(1/2/3/4):")
choose = input("")

print("请输入数字: ")
num1 = int(input(""))
print("请输入最后一个数字:")
num2 = int(input(""))
 
print("结果是:")

if choose == '1':
   print(add(num1,num2))
 
elif choose == '2':
   print(subtract(num1,num2))
 
elif choose == '3':
   print(multiply(num1,num2))
 
elif choose == '4':
   print(divide(num1,num2))
else:
   print("输入错误")