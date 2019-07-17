import collections
import re
import jieba

def stats_text_cn(w):
    if type(w) != str:
        raise ValueError('Oops! That was not a string type. Try again...')
    cn = re.findall(r'[\u4e00-\u9fa5]', w)
    cn_join = ''.join(cn)
    seg_cn = jieba.cut(cn_join)
    seg_words = []
    for element in seg_cn:
        if len(element) > 1:
            seg_words.append(element)
    count = 100
    cn_count = collections.Counter(seg_words).most_common(count)
    return cn_count

def stats_text_en(w):
    if type(w) != w:
        raise ValueError('Oops! That was not a string type. Try again...')
    en = re.findall(r'[a-zA-Z\s]', w)
    en = ''.join(en)
    en = en.split()
    count = 200
    en_count = collections.Counter(en).most_common(count)
    return en_count

def stats_text(w):
    text_count = stats_text_cn+stats_text_en
    return text_count
