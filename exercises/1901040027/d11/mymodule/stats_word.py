
import re
import collections
from collections import Counter
import jieba


def stats_text_cn(text): 
    word_list = []
    count_list = []
    cn_pattern = re.compile(r'[\u4e00-\u9fa5]')
    text_cn = re.findall(cn_pattern, text)
    text_cut = ''.join(text_cn)
    word_list = [x for x in jieba.cut_for_search(text_cut) if len(x) >= 2] #精准模式分词
    count_list = Counter(word_list).most_common(20) #按词频排序并用count控制输出
    return count_list
