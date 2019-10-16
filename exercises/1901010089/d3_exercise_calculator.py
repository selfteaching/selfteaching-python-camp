def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
print('******************************')
print("简陋计算器---只能算加减乘除哦")
print('******************************')
num1 = int(input("输入第一个数字:"))
print("使用哪种运算？1:+  2:-  3:*  4:/")
choice = input("输入您的选择（1、2、3、4）：")
num2 = int(input("输入第二个数字:"))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2),)
 
elif choice == '2':
   print(num1,"-",num2,"=", sub(num1,num2))
 
elif choice == '3':
   print(num1,"*",num2,"=", mul(num1,num2))
 
elif choice == '4':
   print(num1,"/",num2,"=", div(num1,num2))
else:
   print("非法输入")