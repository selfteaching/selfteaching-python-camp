#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:31:31 2019

@author: mtattoo
"""
text = input('请输入英文文本:')

# 封装统计英文单词词频的函数
def stats_text_en( text ):
    # 统计输入英⽂单词出现的次数，最后返回⼀个按词频降序排列列的数组
    import re #引入库
    text_pure = re.sub(r'[^\w\s]','',text)  #正则表达式进行剔除
    words = text_pure.split()  # 拆分所有单词

    frequency= {}  # 定义频率字典
    for word in words:
        if word not in frequency:
            frequency [word] = 1
        else:
            frequency [word] += 1
    frequency_order = sorted(frequency.items(),key = lambda item:item[1],reverse = True)
    print('您此次输入的文本词频降序排列如下:', frequency_order)
stats_text_en( text )  # 执行封装函数


text = input('请输入中文文本:')
# 封装统计中文汉字次数的函数
def stats_text_cn( text ):
    cn_characters = []
    for character in text:
        # 以unicode中中文字符存储的范围
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    frequency= {}  # 定义频率字典
    for cn_characters in text:
        if cn_characters not in frequency:
            frequency [cn_characters] = 1
        else:
            frequency [cn_characters] += 1
    frequency_order = sorted(frequency.items(),key = lambda item:item[1],reverse = True)
    print('您此次输入的文本词频降序排列如下:', frequency_order)

stats_text_cn( text ) # 执行封装函数