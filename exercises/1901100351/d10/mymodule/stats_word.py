# this is d10 exercise for using the third lib
# date: 2019.09.28
# author by: rtgong

import collections
import re
import jieba
from collections import Counter


# 统计参数中英文单词出现的次数，并按降序排列
def stats_text_en(text, count):  #定义函数
    elements = text.split()
    words = []
    symbols = ',.!-*?'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        #isascii() 表示如果字符串为空或者所有字母都是ASCII字符则返回True，否则返回False
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)


# 统计参数中汉字出现次数，并按降序排列
def stats_text_cn(text, count):

    words = jieba.cut(text)
    tmp = []
    for i in words:
        if len(i)>1:
            tmp.append(i)
    return Counter(tmp).most_common(count)

    

# 合并英汉词频统计
def stats_text(text,count) :
    '''
    合并英文词频 和 中文字频 的结果
    '''
    
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型,输入类型 %s' % type(text))
    return stats_text_en(text,count) + stats_text_cn(text,count)
