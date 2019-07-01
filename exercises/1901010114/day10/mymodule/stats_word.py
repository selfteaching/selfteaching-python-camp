import re
from collections import Counter
import jieba
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
    cn = re.sub(r'[\Wa-zA-Z0-9]','',text) 
    cn_1 = jieba.cut(cn, cut_all=False)  #用jieba第三方库对cn进行分词而不是分字
    list_cn = []  #建立一个空列表，为下一个循环使用
    for i in cn_1:
        if len(i)>= 2:
            list_cn.append(i)

    return Counter(list_cn).most_common(count)

def stats_text(text,count):
    list_en = stats_text_en(text,count)
    list_cn = stats_text_cn(text,count)

    return list_en + list_cn


