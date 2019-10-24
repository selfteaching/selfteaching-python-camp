# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:51:15 2019

"""
import stats_word
#text=input('请输入英文:\n')
def a(text): 
    try:  
        stats_word.stats_text_en(text)
    except ValueError:
        raise ValueError('请确认输入英文')
    return
#a(text)
        
text1=input('请输入中文:\n')
def b(text1):
    try:   
        stats_word.stats_text_cn(text1)
    except ValueError:
        raise ValueError('请确认输入中文')
    return
b(text1)
