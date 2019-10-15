def add(x,y):
    return x+y
def chen(x,y):
    return x*y
def jian(x,y):
    return x-y
def chu(x,y):
    return x/y
print("运算算法：")
print("1,相加")
print("2,相乘")
print("3,相减")
print("4,相除")
choice=input("输入你的选择1/2/3/4：")
num1=int(input("输入第一个数字："))
num2=int(input("输入第二个数字："))
if choice=="1":
   print(add(num1,num2))
elif choice=="2":
   print(chen(num1,num2))
elif choice=="3":
   print(jian(num1,num2))
elif choice=="4":
   print(chu(num1,num2))
else:
    print("非法输入")