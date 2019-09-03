

from collections import Counter
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
    retext1 = text.replace('，' , ' ').replace('。' , ' ').replace('：' , ' ').replace('！' , ' ').replace('\n', ' ').replace('？', ' ')
    sptext1 = list(retext1)
    cnt=Counter()
    for i in sptext1:
        if u'\u4e00' <= i <= u'\u9fa5':         
            cnt[i]+=1
    return Counter(cnt).most_common(count)

def stats_text(text,count):
    if isinstance(text,str) == False:
        raise TypeError('Invalid string')
    return(stats_text_en(text,count)+stats_text_cn(text,count))