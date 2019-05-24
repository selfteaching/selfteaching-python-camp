import re
from collections import Counter
# 统计英文
def stats_text_en(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型')
    word_list = re.findall(r'\b[a-z]+\'?[a-z]+',text.lower()) 
    cnt_en = Counter()
    for word in word_list:
        cnt_en[word] += 1
    return cnt_en

# 统计中文
def stats_text_cn(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型')
    text_cn = re.sub(r'[\Wa-zA-Z0-9]','',text) 
    cnt_cn = Counter()
    for character in text_cn:
        cnt_cn[character] += 1
    return cnt_cn

def stats_text(text):
    list_en = stats_text_en(text)
    list_cn = stats_text_cn(text)
    return list_en + list_cn


