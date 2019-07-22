
def add(x,y):
      return x + y


def subtract(x,y):
  return x - y

def multiply(x,y):
  return x * y

def divide(x,y):
  return x / y


# 用户输入# 用户输入

print("选择运算：") 
print("1.相加")
print("2.相减")
print("3.相乘") 
print("4.相除")            
choice = input("输入你的选择（1/2/3/4): ")
num1 = int(input("x="))
num2 = int(input("y="))
if choice == '1':
  print("num1" + "num2", "=", add(num1,num2))
elif choice == '2':
  print("num1" - "num2", "=", subtract(num1,num2))
elif choice == '3':
  print("num1" * "num2", "=", multiply(num1,num2)
  elif choice == '4':
   if "num2" == 0:
      print("除数为0，无意义") 
   else:
      print("num1" / "num2", "=",divide(num1, num2))

else:
   print("非法输入")