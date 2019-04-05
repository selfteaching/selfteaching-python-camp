def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("选择运算方式：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")
choice=input("输入你的选择(1、2、3、4、):")
num1=int(input("输入第一个数字："))
num2=int(input("输入第二个数字："))
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