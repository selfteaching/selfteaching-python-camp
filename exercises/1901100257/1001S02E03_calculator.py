# This is a python language calculator
operator = input("请输入运算符（+、-、*、/）:")
first_number = input("请输入第一个数字:")
second_number = input("请输入第二个数字:")

a = int(first_number)
b = int(second_number)

print ("选择运算:")
print("+,相加")
print("-,相减")
print("*,相乘")
print("/,相除")

def add(a,b):
   return a + b

def subtract(a,b):
   return a - b

def multiply(a,b):
   return a * b

def divide(a,b):
   return a / b

if operator =="+":
    print (a,"+",b,"=",a + b)
elif operator =="-":
    print (a,"-",b,"=",a - b)
elif operator =="*":
    print (a,"*",b,"=",a * b)
elif operator =="/":
    print (a,"/",b,"=",a / b)
else:
    print("非法输入")