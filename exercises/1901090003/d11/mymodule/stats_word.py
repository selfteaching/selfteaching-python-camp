import re
import jieba
from collections import Counter
# 统计英文
def stats_text_en(text,count):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型')
    word_list = re.findall(r'\b[a-z]+\'?[a-z]+',text.lower())
    return Counter(word_list).most_common(count)

# 统计中文
def stats_text_cn(text,count):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型')
    text_cn = re.sub(r'[\Wa-zA-Z0-9]','',text) 
    # len 这个函数是判断一个数据的长度，比如一个列表之类的。里面不能加判断条件
    # 底下你看到的 [x for x in jieba.cut(text_cn) if len(x) > 2] 
    # 这指的是列表推导式，你可以去尝试了解一下
    # 可以关掉了
    charater_list = [x for x in jieba.cut(text_cn) if len(x) > 2] 
    return Counter(charater_list).most_common(count)

def stats_text(text,count):
    list_en = stats_text_en(text,count)
    list_cn = stats_text_cn(text,count)
    return list_en + list_cn


