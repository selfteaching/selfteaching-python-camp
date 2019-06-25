
from collections import Counter
import jieba

import re

count = 100

def stats_text_en (text,count):
    if isinstance(text,str) == False:
        raise TypeError('Invalid string')
    retext = text.replace(',',' ').replace('.',' ').replace('--','').replace('!','').replace('*',' ').replace('?','').replace('”','').replace('“','').replace('\n','').lower()
    sptext = retext.split()
    cnt = Counter()
    for i in sptext:
        if i.isascii():
            cnt[i]+=1
    return Counter(cnt).most_common(count)

def stats_text_cn(text,count):
    if isinstance(text,str) == False:
        raise TypeError('Invalid string')
    text = re.sub('[^\u4e00-\u9fa5]','',text)
    seg_list = jieba.cut(text,cut_all = False)
    seg = [word for word in seg_list if len(word)>=2]
    # 下面的Counter接收的参数是列表
    str_cn = str(Counter(seg).most_common(count))
    return str_cn

def stats_text(text,count):
    if isinstance(text,str) == False:
        raise TypeError('Invalid string')
    return(stats_text_en(text,count)+stats_text_cn(text,count))
