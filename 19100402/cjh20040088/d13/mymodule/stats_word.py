import jieba
import collections
import re
def stats_text_en(txt,count):
    if type(txt)==str:
        txt=re.sub('[^A-Za-z]','',txt)
        txt=txt.lower()
        txt=txt.split()
        print(collections.Counter(txt).most_common(count))
    else:
        raise ValueError

def stats_text_cn(txt,count):
    if type(txt)==str:
        txt=re.sub('[^\u4e00-\u9fa5]','',txt)
        txt=txt.strip()
        txt=[x for x in jieba.cut_for_search(txt)]
        print(collections.Counter(txt).most_common(count))
    else:
        raise ValueError

def stats_text(txt,count):
    stats_text_en(txt,count)
    stats_text_cn(txt,count)
