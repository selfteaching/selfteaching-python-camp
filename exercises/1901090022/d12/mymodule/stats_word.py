import re
from collections import Counter
import jieba
def stats_text_en(text, count):
    """统计英文文本的词频
    
    返回list形式的数据"""
    if not isinstance(text, str) :
        raise ValueError("text 必须是 str 类型")
        
    c = Counter()
    for word in text.split():
        match_obj = re.search('([a-zA-Z]+)', word)
        if match_obj is not None:
            w = match_obj.group(1).lower()
            c[w] += 1

    return c.most_common(count)

def stats_text_cn(text, count):
    """统计中午文本的字频
    
    返回list形式的数据"""
    if not isinstance(text, str) :
        raise ValueError("text 必须是 str 类型")

    seg_list = jieba.cut(text)

    c = Counter()
    for word in seg_list:
        if len(word) >= 2:
            c[word] += 1
    return c.most_common(count)

def stats_text(text, count):
    """统计中文、英文文本的词频
    
    返回list形式的数据"""
    if not isinstance(text, str) :
        raise ValueError("text 必须是 str 类型")

    word_list_en = stats_text_en(text, count)
    word_list_cn = stats_text_cn(text, count)
    return word_list_cn + word_list_en
    # return sorted(word_list_en + word_list_cn, key=lambda item:item[1], reverse=True)
