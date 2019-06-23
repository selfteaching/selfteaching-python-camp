#2019.04.03
#与main函数协同更改

'''调用collections的Counter函数'''
import collections
from os import path
import json
import re
'''导入jieba'''
import jieba

def stats_text_en(text):
    #dict1 = {}
    import re
    ''' 保留英文单字 '''
    en_pattern = re.compile(r'[a-zA-Z]+[\'\-]?[a-zA-Z]+')
    list1 = re.findall(en_pattern, text)
    
    return list1

def stats_text_cn(text):
    #dict1 = {}
    ''' 保留中文单字 '''
    cn_pattern = re.compile(r'[\u4e00-\u9fa5]')
    return "".join(re.findall(cn_pattern, text))
    
    #'''调用collections的Counter函数'''
    #cnt = collections.Counter()
    #for word in list1:
        #cnt[word] += 1


def jiebacut(text):
    list2=[]
    seg_list = jieba.cut(text, cut_all=False)
    for i in seg_list:
        if len(i)>=2:
            list2.append(i)
    return list2


def cut_cnwords(text):
    list2=[]
    seg_list = jieba.cut(text, cut_all=True)

    for i in seg_list:
        if len(i)>=2:
            list2.append(i)
    return list2

def stats_text(text):
    '''使用isinstance函数验证输入的参数类型是否为str'''
    if isinstance(text, str) != True: 
        '''用raise语句来引发异常'''
        raise ValueError
    else: 
        return stats_text_en(text),stats_text_cn(text)

def main(text):
    '''提取所有英文单字'''
    enwords = stats_text_en(text)
    '''提取所有中文单字'''
    cnwords = stats_text_cn(text)
    '''分词'''
    cutcnwords = cut_cnwords(cnwords)
    return enwords+cutcnwords