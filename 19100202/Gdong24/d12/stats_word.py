#引用package
import jieba
import collections 
from collections import Counter 
import re


#中文词频排序
def stats_text_cn(text2):
    #建立列表 local varialbe 
    cut_list = []
    word_list = []
    count_list = []
    
    cn_pattern = re.compile(r'[\u4e00-\u9fa5]')
    text_cn = re.findall(cn_pattern, text2)
    
    text_cut = ''.join(text_cn)                      #把筛选返回的list转为str
    
    cut_list = jieba.cut(text_cut,cut_all=False)    #使用jieba精准模式分词
    
    for word in cut_list:                            #筛选大于等于2字的词
        if len(word) >= 2:
            word_list.append(word)
    #用counter优化输出(day9)
    count_list = Counter(word_list).most_common(100)
    return count_list
