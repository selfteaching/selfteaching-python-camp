# 这是邓超抄写的第一个简单程序
# 可以运算加减乘除的简易计算器


# 用户输入
print("选择运算，")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")

a = int(input("请输入第一个数字："))

choice = input("请输入你的选择(1/2/3/4):")

b = int(input("请输入第二个数字："))

if choice == '1':
    print(a+b)

elif choice == '2':
    print(a-b)

elif choice == '3':
    print(a*b)

elif choice == '4':
    print(a/b)
else:
    print("输入无效")
    