# -*- coding: UTF-8 -*-

import collections
import re


def stats_text_en(en):
    ''' 英文词频统计'''

    if type(en) == str:
        '''参数类型检查,如果输入参数不为字符串则抛出ve'''
        text_en = re.sub("[^A-Za-z]", " ", en.strip())
        enList = text_en.split()
        return collections.Counter(enList)
    else:
        raise ValueError("输入不为字符串")


def stats_text_cn(cn):
    ''' 中文词频统计 '''
    if type(cn) == str:
        '''参数类型检查,如果输入参数不为字符串则抛出ve'''
        cnList = re.findall(u'[\u4e00-\u9fff]+', cn.strip())  # 提取中文
        cnString = cnList.split()  # 或者''.join(cnList) #join（）在每个字符间加空格
        return collections.Counter(cnString)
    else:
        raise ValueError("输入不为字符串")


def stats_text(text_en_cn):
    ''' 合并英汉词频统计 '''
    if type(text_en_cn) == str:
        return (stats_text_en(text_en_cn)+stats_text_cn(text_en_cn))
    else:
        raise ValueError("输入不为字符串")
