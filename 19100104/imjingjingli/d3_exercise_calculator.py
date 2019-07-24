# 定义函数
def add(x, y):
   """
   加法运算
   parameter x: 被加数
   parameter y: 加数
   return x + y: 和
   """
   return x + y


def subtract(x, y):
   """
   减法运算
   parameter x:被减数
   parameter y:减数
   return x - y：差
   """
   return x - y


def multiply(x, y):
   """
   乘法运算
   parameter x:被乘数
   parameter y：乘数
   return x * y:积
   """
   return x * y


def divide(x, y):
   """
   除法运算
   parameter x:被除数
   parameter y:除数
   return x / y:商
   """
   return x / y
 
# 用户输入
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")

while True:  #如果运算结果正确则无限循环
   choice = input("输入你要进行的运算(1/2/3/4):")  
 
   if choice == '1':
      num1 = int(input("输入第一个数字: "))
      num2 = int(input("输入第二个数字: "))
      print(num1,"+",num2,"=", add(num1,num2))
 
   elif choice == '2':
      num1 = int(input("输入第一个数字: "))
      num2 = int(input("输入第二个数字: "))
      print(num1,"-",num2,"=", subtract(num1,num2))
   
   elif choice == '3':
      num1 = int(input("输入第一个数字: "))
      num2 = int(input("输入第二个数字: "))
      print(num1,"*",num2,"=", multiply(num1,num2))
   
   elif choice == '4':
      num1 = int(input("输入第一个数字: "))
      num2 = int(input("输入第二个数字: "))
      print(num1,"/",num2,"=", divide(num1,num2))
   else:
      print("非法输入")