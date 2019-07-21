import re
import collections
import jieba


def stats_text_cn(text): #定义函数，统计汉字计数
    seg_list = list(jieba.cut(text, cut_all=False))
    seg_list_select=[x for x in seg_list if len(x)>=2]
    print(collections.Counter(seg_list_select).most_common(20))