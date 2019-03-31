# -*- coding: UTF-8 -*-
# 2019.03.27

import collections
import re
import jieba  # 3.27
"""创建一个名为stats_text_en的函数"""


def stats_text_en(en, count):
    ''' 英文词频统计'''
    ''' 参数类型检查;如果输入参数不为字符串则抛出ve'''
    if type(en) == str:  # 判断输入的是字符，执行以下语句

        text_en = re.sub("[^A-Za-z]", " ", en.strip())  # 只保留字母，并用空格作为分隔符
        enList = text_en.split()
        # 以空格以及折行为分隔，将每个被分割的内容作为一个列表元素，并将所有列表元素合在一起组成一个列表
        return collections.Counter(enList).most_common(count)
        # 利用colections中的Counter为每个出现的英文单词计数，返回前count个词频最高的词及出现的次数
    else:
        raise ValueError("输入不为字符串")


def stats_text_cn(cn, count):
    ''' 中文词频统计 '''
    '''参数类型检查,如果输入参数不为字符串则抛出ve'''
    '''使用jieba精确模式分词'''  # 3.27
    '''使用for循环判断分词后词频列表元素长度大于等于2的生成新列表。'''  # 3.27
    if type(cn) == str:
        cnList = re.findall(u'[\u4e00-\u9fff]+', cn.strip())  # 提取中文
        seg_list = jieba.cut(' '.join(cnList)) # 精确模式
        cn1 = []
        for i in seg_list:
            if len(i) >= 2:#判断如果大于等于2的字符串就加进cn1数组
                cn1.append(i)
        return collections.Counter(cn1).most_common(count)
        # 利用colections中的Counter为cn1list每个出现的词计数，返回前count个词频最高的词及出现的次数
    else:
        raise ValueError("输入不为字符串")

def stats_text(text_e_c, count_e_c):
    ''' 合并英汉词频统计 '''
    '''参数类型检查,如果输入参数不为字符串则抛出ve'''
    if type(text_e_c) == str:
        return (stats_text_en(text_e_c, count_e_c)+stats_text_cn(text_e_c, count_e_c))
    else:
        raise ValueError("输入不为字符串")
