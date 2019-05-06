#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###################
#函数:stats_text_en(text)
# 统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
####################
def stats_text_en(text):
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
    list2 = list(set(list1))#单词不重复的列表
    list2.sort()#单词从首字母a~z排序
    j=0
    dictData = {}#创建字典
    for word in list2:
        j = list1.count(word)
        dictData[word] = j #生成字典类型

    #print(dictData)
    listTemp = list(set(list(dictData.values()))) #对单词出现的次数进行列表化，去除重复项
    listTemp.sort(reverse = True) #从大到小排列value
    #按词频大小重新排列字典
    dictFinal = {}
    for i in listTemp:
        for key in dictData:
            if dictData[key] == i:
                dictFinal[key] = i #生成新的字典
    listWord = list(dictFinal.items())
    #print(dictFinal)
    return listWord

###################
#函数:stats_text_cn(text)
# 统计参数中每个中文字符出现的次数，最后返回一个按字频降序排列的数组
####################
def stats_text_cn(text):
    "统计参数中每个中文字符出现的次数，最后返回一个按字频降序排列的数组"
    if isinstance(text,str)==False:
        raise ValueError("The input of stats_text_cn() is not string")
    unicodeChineseMin = int('0x4e00',16)
    unicodeChineseMax = int('0x9fa5',16)
    text2 =''
    for i in text:
        if (ord(i)>=unicodeChineseMin and ord(i)<=unicodeChineseMax):
            text2 = text2+i+' ' #去除多余非汉字字符
    list1 =text2.split() #存储text汉字化的列表
    list2 = list(set(list1))#汉字不重复的列表
    j=0
    dictData = {}#创建字典
    for word in list2:
        j = list1.count(word)
        dictData[word] = j #生成字典类型

    #print(dictData)
    listTemp = list(set(list(dictData.values()))) #对汉字出现的次数进行列表化，去除重复项
    listTemp.sort(reverse = True) #从大到小排列value
    #按词频大小重新排列字典
    dictFinal = {}
    for i in listTemp:
        for key in dictData:
            if dictData[key] == i:
                dictFinal[key] = i #生成新的字典
    listWord = list(dictFinal.items())
    #print(dictFinal)
    return listWord

def stats_text(text):
    "统计字符串中中文汉字和英文单词出现的次数，并返回一个按词频降序排列的数组"
    if isinstance(text,str)==False:
        raise ValueError("The input of stats_text() is not string")
    return stats_text_en(text) + stats_text_cn(text)


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
    床前明月光，疑是地上霜。举头望明月，低头思故乡。'''
    print(stats_text_en(text))
    print(stats_text_cn(text))
    print(stats_text(text))
 