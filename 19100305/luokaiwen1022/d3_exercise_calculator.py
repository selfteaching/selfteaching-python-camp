# This is d3_exercise_calculator.py
import string

# this is def of add, sub, mul, div, pow
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        return "Dividend can't be zero.Please input again."
    else:
        return a / b
def pow(a,b):
    return a ** b

# 给出运算选项
print("可进行的运算法：")
print("1.加")
print("2.减")
print("3.乘")
print("4.除")
print("5.乘方")

#给出四则运算选项
choice = input("请选择要进行的运算（1， 2, 3， 4， 5）：")
num1 = float(input("请输入要运算的数字1："))#要求输入要运算的第一个数字
num2 = float(input("请输入要运算的数字2："))#要求输入要运算的第二个数字

if choice == '1':#如果选择加法运算
    print(num1,"+",num2,"=",add(num1,num2))#列出计算式和计算的结果
elif choice == '2':#如果选择减法运算
    print(num1,"-",num2,"=",sub(num1,num2))#列出计算式和计算的结果
elif choice == '3':#如果选择乘法运算
    print(num1,"*",num2,"=",mul(num1,num2))#列出计算式和计算的结果
elif choice == '4':#如果选择除法运算
    print(num1,"/",num2,"=",div(num1,num2))#列出计算式和计算的结果
elif choice == '5':#如果选择乘方运算
    print(num1,"**",num2,"=",pow(num1,num2))#列出计算式和计算的结果
else:
    print("请输入正确的数字或选择给定的运算方式")#如果输入错误的给出处理建议