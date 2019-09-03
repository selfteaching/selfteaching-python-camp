#简易版本计算器

# 加
def add(x, y):
    return x + y

# 减
def subtract(x, y):
   return x - y

# 乘
def multiply(x, y)：
   return x * y

# 除
def divide(x, y)
   return x / y

print("选择对应的运算方式")
print("1.加")
print("2.减")
print("3.乘")
print("4.除")

choice = input("输入（1/2/3/4):")

num1 = int(input("输入第一个数字"))
num2 = int(input("输入第一个数字"))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice =='2':
   print(num1, "+", num2, "=", subtract(num1, num2))

elif choice =='3':
   print(num1, "+", num2, "=", multiply(num1, num2))

elif choice =='4':
   print(num1, "+", num2, "=", divide(num1, num2))

else:
   print("错误输入")
