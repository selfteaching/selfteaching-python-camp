import re
import collections
from collections import Counter
import jieba

def stats_text_ch(text):
    cut_list = []
    word_list = []
    count_list = []

    ch_pattern = re.compile(r'[\u4e00-\u9fa5]')
    text_ch = re.findall(ch_pattern,text)

    text_cut = ''.join(text_ch)                                                #把筛选返回的list转为str

    cut_list = jieba.cut(text_cut,cut_all=False)                               #使用jieba精准模式分词

    for word in cut_list:
        if len(word)>=2:
            word_list.append(word)
    count_list=Counter(word_list).most_common(20)
    return count_list


   