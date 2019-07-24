a=int()
b=int()
import re
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("请选择运算：")
print("1:加法运算")
print("2:减法运算")
print("3:乘法运算")
print("4:除法运算")
choice=input("请输入你想要进行的运算代码(1/2/3/4):")
num1=int(input("请输入第一个数字:"))
num2=int(input("请输入第二个数字:"))
if choice=='1':
   print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
   print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
   print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
   print(num1,"/",num2,"=",divide(num1,num2))
else:
   print("非法输入")