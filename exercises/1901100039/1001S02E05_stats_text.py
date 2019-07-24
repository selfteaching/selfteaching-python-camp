#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 18:10:33 2019

@author: mtattoo
"""

# 字符串的统计

text ='''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

# 统计文本中单词出现的次数

import re #引入库
text_pure = re.sub(r'[^\w\s]','',text)  #正则表达式进行剔除
words = text_pure.split()  # 拆分所有单词

frequency= {}  # 定义频率字典
for word in words:
    if word not in frequency:
        frequency [word] = 1
    else:
        frequency [word] += 1
print (frequency)

# 按统计次数输出
frequency_order = sorted(frequency.items(),key = lambda item:item[1],reverse = True)
print(frequency_order)
