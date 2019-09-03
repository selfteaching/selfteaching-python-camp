
import os, codecs
import jieba
from collections import Counter
import re

def stats_text_en(text):
    """统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组"""
    if not isinstance(text,str):
        raise ValueError(f'输入的参数是{type(text)}类型，不是字符串类型。')
    string=text
    text_1=re.sub(u'[\u4e00-\u9fa5，。？?.！：,、“”]', " ",string)
    seg_list = text_1.split()
    c = Counter()
    for x in seg_list:
        if len(x)>1 and x != '\r\n':
            c[x] += 1
    print('常用词频度统计结果:')
    result=[]
    for (k, v) in c.most_common(100):
        a = f'{k} {v}'
        result.append(a)
    return result

def stats_text_cn(text):
    """统计参数中每个中文汉字出现的次数，最后返回一个按字频降序排列的数组"""
    if not isinstance(text,str):
        raise ValueError(f'输入的参数是{type(text)}类型，不是字符串类型。')
    string=text
    text_0=re.sub('[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", string)

    seg_list = jieba.cut(text_0)
    c = Counter()
    for x in seg_list:
        if len(x)>1 and x != '\r\n':
            c[x] += 1
    print('常用词频度统计结果:')
    result=[]
    for (k, v) in c.most_common(100):
            b = f'{k} {v}'
            result.append(b)
    return result

def stats_text(text):
    """分别调用stats_text_en , stats_text_cn ，输出合并词频统计结果"""
    if not isinstance(text,str):
        raise ValueError(f'输入的参数是{type(text)}类型，不是字符串类型。')
    if type(text) == str:
        return(stats_text_en(text)+stats_text_cn(text))
  
