a = int(input("输入第一个数字: "))
# 用户输入
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")
 
choice = input("输入你的选择(1/2/3/4):")
 
b = int(input("输入第二个数字: "))
 
if choice == '1':
   print(a+b)
 
elif choice == '2':
   print(a-b)
 
elif choice == '3':
   print(a*b)
 
elif choice == '4':
   print(a/b)
else:
   print("非法输入")