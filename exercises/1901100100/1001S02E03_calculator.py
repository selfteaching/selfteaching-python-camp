# 这是一个进行简单四则运算的程序
import sys
result = 0
while True:
    firstnum = float(input("请输入一个数字"))
    symbol = input("请输入运算符号+、—、*、/")
    secondnum = float(input("请再输入一个数字"))
    if symbol == "+":
        result = firstnum+secondnum
    elif symbol == "-":
        result = firstnum-secondnum
    elif symbol == "*":
        result = firstnum*secondnum
    elif symbol =="/":
        result = firstnum/secondnum
    else:
        print("请输入正确的运算符")

    #result = firstnum*secondnum
    print (result)
    print("继续运行，请按y")
    d = input()
    if d!="y":
        break