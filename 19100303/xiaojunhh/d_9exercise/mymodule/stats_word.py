# -*- coding: UTF-8 -*-
# Day9 重新修改

import collections
import re

"""创建一个名为stats_text_en的函数"""
def stats_text_en(en,count):
    ''' 英文词频统计'''
    ''' 参数类型检查;如果输入参数不为字符串则抛出ve'''
    if type(en) == str: #判断输入的是字符，执行以下语句

        text_en = re.sub("[^A-Za-z]", " ", en.strip())#只保留字母，并用空格作为分隔符
        enList = text_en.split()
        #以空格以及折行为分隔，将每个被分割的内容作为一个列表元素，并将所有列表元素合在一起组成一个列表
        return collections.Counter(enList).most_common(count)
        #利用colections中的Counter为每个出现的英文单词计数，返回前count个词频最高的词及出现的次数
    else:
        raise ValueError("输入不为字符串")


def stats_text_cn(cn,count):
    ''' 中文词频统计 '''
    '''参数类型检查,如果输入参数不为字符串则抛出ve'''
    if type(cn) == str:
        
        cnList = re.findall(u'[\u4e00-\u9fff]+', cn.strip())  # 提取中文
        cnString = ''.join(cnList) 
        return collections.Counter(cnString).most_common(count)
        #利用colections中的Counter为每个出现的英文单词计数，返回前count个词频最高的词及出现的次数
    else:
        raise ValueError("输入不为字符串")


def stats_text(text_e_c,count_e_c):
    ''' 合并英汉词频统计 '''
    '''参数类型检查,如果输入参数不为字符串则抛出ve'''
    if type(text_e_c) == str:
        return (stats_text_en(text_e_c,count_e_c)+stats_text_cn(text_en_cn,count_e_c))
    else:
        raise ValueError("输入不为字符串")

# 尝试了多次都无法同步作业库.....
