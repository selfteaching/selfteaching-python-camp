import jieba
import collections

from collections import Counter






count = int()
def stats_text_en(text,count):
    import re
    text_en = re.sub("[^A-Za-z]", " ", text.strip())
    list_en = text_en.split()
    return collections.Counter(list_en)
def stats_text_cn(text,count):
    import re
    text_cn = re.findall(u'[\u4e00-\u9fff]+', text.strip())
    str_cn = ''.join(text_cn)
    seg_list = jieba.cut(str_cn)
    nlist = []
    for i in seg_list:
        if len(i)>=2:
            nlist.append[i]
        else:
            pass

    return collections.Counter(nlist).most_common(count)

def stats_text(text,count):
    return collections.Counter(stats_text_en(text,count)+stats_text_cn(text,count)).most_common(count)


