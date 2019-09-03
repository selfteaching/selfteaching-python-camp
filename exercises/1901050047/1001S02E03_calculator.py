# 一个支持加、减、乘、除功能的计算器
print("这是一个python计算器")
print("加法运算输入：1")
print("减法运算输入：2")
print("乘法运算输入：3")
print("除法运算输入：4")
a = int(input("请输入第一个数字："))  
b = int(input("请输入第二个数字："))
i = int(input("请选择运算符号（1、2、3、4）："))
if i == 1:
    print(f'加法结果为 {a+b}')
elif i == 2: 
    print(f'减法结果为 {a-b}')
elif i == 3:  
    print(f'乘法法结果为 {a*b}')
elif i == 4:
    print(f'除法结果为 {a/b}')
else:
    print(f'输入错误,程序终止')