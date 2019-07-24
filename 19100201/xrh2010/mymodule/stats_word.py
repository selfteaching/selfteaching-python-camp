
import collections
from collections import Counter
count = int()
def stats_text_en(text,count):
    import re
    text_en = re.sub("[^A-Za-z]", " ", text.strip())
    list_en = text_en.split()
    return collections.Counter(list_en)

def stats_text_cn(text,count):
    import jieba
    seg_list = jieba.cut(text)
    return collections.Counter(seg_list)
def stats_text(text,count):
    return collections.Counter(stats_text_en(text,count)+stats_text_cn(text,count)).most_common(count)  





