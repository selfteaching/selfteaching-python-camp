def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y

print("请按以下提示选择运算：")
print("1：加")
print("2：减")
print("3：乘")
print("4：除")
choice = input("请输入你的选择(1/2/3/4):")
if choice > "4":
    print("你的输入有误！")
else:
    num1 = int(input("请输入第一个数字: "))
    num2 = int(input("请输入第二个数字: "))
if choice == '1':
   print("运算结果为:",num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print("运算结果为:",num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print("运算结果为:",num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print("运算结果为:",num1,"/",num2,"=", divide(num1,num2))