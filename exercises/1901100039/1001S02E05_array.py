#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:21:21 2019

@author: mtattoo
"""

# 定义数组
list_0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_1 = list_0[::-1]  # 逆转数组
print(list_1)

# 拼接字符串
list_2 = [str(i) for i in list_1]# 使用列表推导式把列表中的单个元素全部转化为str类型
list_3 = ''.join(list_2)
print (list_3)

# 取出第三到第八个字符
list_4 = list_3[2:8]  # 字符串以0开始，参数最后一位数据不计入列表，故不是2:7
print (list_4)

# 对字符串进行翻转
list_r = list_4[::-1]
print (list_r)

# 将结果转化为int类型

int_value = int(list_r)

print(int_value)

# 将结果转化为二进制，八进制和十六进制，并输出

print("转换为二进制的值：", bin(int_value))
print("转换为八进制的值：", oct(int_value))
print("转换为十六进制的值：", hex(int_value))