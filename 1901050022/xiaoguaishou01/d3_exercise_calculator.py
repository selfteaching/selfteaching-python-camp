#使用Python编写一个支持加、减、乘、除功能的计算器，支持输入参数，支持输出结果。
# 定义函数
def add(x, y):#加法
   return x + y 

def subtract(x, y):#减法
   return x - y 

def multiply(x, y):#乘法
   return x * y 

def divide(x, y): #除法
   return x / y 

# 用户输入
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")
choice = input("输入你的选择(1/2/3/4):") 
num1 = float(input("输入第一个数字: "))
num2 = float(input("输入第二个数字: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2)) 
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2)) 
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2)) 
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("非法输入")
#这个是简单版本，我只会定义函数，后面有些是从Google借鉴的，先提交作业，晚上再慢慢消化

   