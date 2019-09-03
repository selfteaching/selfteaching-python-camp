#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter
import jieba
###################
#函数:stats_text_en(text,count = None)
# 统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
####################
def stats_text_en(text, count = None):
    '统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组'
    if isinstance(text,str)==False:
        raise ValueError("The input of stats_text_en() is not string")
    text1 = text.lower()#单词小写化

    alphaList="abcdefghijklmnopqrstuvwxyz "#英文字母表，后期可改成unicode编码方式
    puncList="\"\n\\-!“”?,，。.*%\t\r" #英文或中文标点转换成空格，为防止text的不规范
    text2 =''
    for i in text1:
        if i in alphaList:
            text2 = text2+i #去除多余非字母字符
        elif i in puncList:
            text2 = text2 + ' '
    list1 =text2.split() #存储text单词化的列表
    dictFinal = Counter(list1) #Counter计数
    #print(type(dictFinal))
    listWord = dictFinal.most_common(count) #返回词频最高的count个
    return listWord

###################
#函数:stats_text_cn(text,count = None, len_size = 1)
# 统计参数中每个中文字符出现的次数，最后返回一个按字频降序排列的数组
# text:需要统计的字符串
# count:统计词频出现最高的前count个
# len_size: 中文词的最小长度，长度小于len_size的词不统计
####################
def stats_text_cn(text, count = None, len_size = 1):
    "统计参数中每个中文字符出现的次数，最后返回一个按字频降序排列的数组"
    if isinstance(text,str)==False:
        raise ValueError("The input of stats_text_cn() is not string")#如果不是字符串则提示错误
    unicodeChineseMin = int('0x4e00',16)
    unicodeChineseMax = int('0x9fa5',16)
    text1 =''
    for i in text:
        if (ord(i)>=unicodeChineseMin and ord(i)<=unicodeChineseMax):
            text1 = text1+i #去除多余非汉字字符
        else:
            text1 = text1+' '
    text2 = jieba.cut(text1) #jieba分词
    #print(type(text2))
    word_list = " ".join(text2) 
    list1 =word_list.split() #存储text汉字化的列表
    list_Final = []
    for i in list1:           #词的长度小于len_size不统计
        if len(i)>=len_size:
            list_Final.append(i)

    dictFinal = Counter(list_Final)
    listWord = dictFinal.most_common(count) #返回词频最高的count个
    return listWord

def stats_text(text, count = None, len_size = 1):
    "统计字符串中中文汉字和英文单词出现的次数，并返回一个按词频降序排列的数组"
    if isinstance(text,str)==False:
        raise ValueError("The input of stats_text() is not string")
    return stats_text_en(text,count) + stats_text_cn(text,count,len_size)



if __name__ == "__main__": #模块测试部分
    text = ''' 
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
    床前明月光，疑是地上霜。举头望明月，低头思故乡。清华大学，北京大学'''
   # print(stats_text_en(text,10))
    print(stats_text_cn(text,10,len_size=2))
    #print(stats_text(text,10,2))
 