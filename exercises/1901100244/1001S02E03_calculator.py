# -*- coding: UTF-8 -*-

# Filename : 1001S02E03_calculator.py
# author by : @shen-huang

# 一个支持 加、减、乘、除功能 的计算器，支持输入参数，支持输出结果

def add(x, y):
    print("{} + {} = ".format(x,y))
    print(x + y)

def sub(x, y):
    print("{} - {} = ".format(x,y))
    print(x - y)

def mul(x, y):
    print("{} × {} = ".format(x,y))
    print(x * y)

def div(x, y):
    if y == 0:
        print("输入错误，除数不能为0！")
    else:
        print("{} ÷ {} = ".format(x,y))
        print(x / y)

x = float(input("请输入第一个数字: "))
y = float(input("请输入第二个数字: "))
a = input("请选择运算（+ - * /）: ")

if a == '+':
    add(x, y)
elif a == '-':
    sub(x, y)
elif a == '*':
    mul(x, y)
elif a == '/':
    div(x, y)
else:
    print('输入错误！')