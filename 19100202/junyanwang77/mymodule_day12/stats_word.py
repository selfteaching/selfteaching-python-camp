import re
import collections
from collections import Counter
import jieba
   

def stats_text_cn(text):
        cut_list = []
        cut_list = []
        word_list = []
        count_list = []

        cn_pattern = re.compile(r'[\u4e00-\u9fa5]')
        text_cn = re.findall(cn_pattern,text)
        text_cut = ''.join(text_cn)
        cut_list = jieba.cut(text_cut,cut_all=False) 

        for word in cut_list:
                if len(word)>=2:
                        word_list.append(word)

        count_list=Counter(word_list).most_common(100)
        return count_list
 
