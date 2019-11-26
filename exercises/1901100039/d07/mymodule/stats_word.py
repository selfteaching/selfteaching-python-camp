#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:31:31 2019

@author: mtattoo
"""

# 封装统计英文单词词频的函数
def stats_text_en(text):
    # 统计输入英⽂单词出现的次数，最后返回⼀个按词频降序排列列的数组
    elements = text.split() # 拆分所有单词
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')  # 剔除字符
        # 用str 类型的 isascii 方法判断是否英文单词
        if len(element) and element.isascii():
            words.append(element)
    counter = {}
    word_set = set(words)
    
    for word in word_set:
        counter[word] = words.count(word)
    return sorted(counter.items(),key = lambda x: x[1],reverse = True)

# 封装统计中文汉字次数的函数
def stats_text_cn(text):
    cn_characters = []
    for character in text:
        # 以unicode中中文字符存储的范围
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    counter = {}  
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(),key = lambda x: x[1],reverse = True)


def stats_text( text ):
    '''
    合并显示中文及英文字符数量
    '''
    return stats_text_en(text) + stats_text_cn(text)