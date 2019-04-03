#coding=gbk
def jia(x, y):
	return x + y
def jian(x, y):
	return x - y
def cheng(x, y):
	return x * y
def chu(x, y):
	return x/y

num1 = int(input("输入第一个数字："))
print("选择运算:")
print("1:加")
print("2:减")
print("3:乘")
print("4:除")
choice = input("选择运算类型(1/2/3/4):")
num2 = int(input("输入第二个数字： "))
if choice == '1':
	print(num1,"+",num2,"=", jia(num1,num2))
elif choice == '2':
	print(num1,"-",num2,"=",jian(num1,num2))
elif choice == '3':
	print(num1,"*",num2,"=",cheng(num1,num2))
elif choice == '4':
	print(num1,"/",num2,"=",chu(num1,num2))
else:
	pint("非法输入")
