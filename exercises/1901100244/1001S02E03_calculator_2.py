# -*- coding: UTF-8 -*-

# Filename : 1001S02E03_calculator_2.py
# author by : @shen-huang

# 一个支持 常见数学运算功能 的计算器，支持输入参数，支持输出结果

# 直接使用 print(eval(input())) 也可完成需求，
# 考虑安全性和用户友好等问题后，添加了其他代码。

import math

ALLOWED = {v: getattr(math, v)
for v in filter(lambda x: not x.startswith('_'), dir(math))
}

while 1:
    str = input("请输入要计算的算式，回车运算，退出请按“Q”：\n")
    try:
        if str == "Q":
            print("感谢您的使用！再见！")
            break
        elif str == "q":
            print("感谢您的使用！再见！")
            break
        else:
            print("{0} = {1}".format(str, eval(str, ALLOWED, {})))
    except ZeroDivisionError:
        print("错误：除数不能为 0！")
    except SyntaxError:
        print("错误：请正确输入算式！")
    except NameError:
        print("错误：只接受数学算式！")
    except:
        print("错误：Something Happend!")
