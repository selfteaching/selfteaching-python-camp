
import os, codecs
import jieba
import collections
from collections import Counter
import re

def stats_text_en(text,count):
    """统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组"""
    if isinstance(text,str):    
        string=text   
        text_1=re.sub(u'[\u4e00-\u9fa5，。？?.！：,、“”]', " ",string)
        seg_list = text_1.split()
        x=int(count)
        y=len(seg_list)
        x <= y
        tuple_0=tuple(seg_list)
        return collections.Counter(tuple_0).most_common(100)
    else:
        print(f'输入的参数是{type(text)}类型，不是字符串类型。')



def stats_text_cn(text,count):
    """统计参数中每个中文汉字出现的次数，最后返回一个按字频降序排列的数组"""
    if isinstance(text,str):
        string=text
        text_0=re.sub('[a-zA-Z0-9’!"#$%&\'()*+,-.：/:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", string)
        seg_list_1 = list(jieba.cut(text_0))
        x=int(count)
        y=len(seg_list_1)
        x <= y
        tuple_1=tuple(seg_list_1)
        return collections.Counter(tuple_1).most_common(100)
    else:
        print(f'输入的参数是{type(text)}类型，不是字符串类型。')

    

def stats_text(text,count):
    """分别调用stats_text_en , stats_text_cn ，输出合并词频统计结果"""
    if not isinstance(text,str):
        raise ValueError(f'输入的参数是{type(text)}类型，不是字符串类型。')
    if type(text) == str:
        return(stats_text_en(text,count)+stats_text_cn(text,count))
