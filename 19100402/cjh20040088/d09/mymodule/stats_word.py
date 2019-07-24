import collections
def stats_text_en(txt,count):
    import re
    if type(txt)==str:
        txt=re.sub('[^A-Za-z]','',txt)
        txt=txt.lower()
        txt=txt.split()
        print(collections.Counter(txt).most_common(count))
    else:
        raise ValueError

def stats_text_cn(txt,count):
    import re
    if type(txt)==str:
        txt=re.sub('[^\u4e00-\u9fa5]','',txt)
        txt=txt.strip()
        print(collections.Counter(txt).most_common(count))
    else:
        raise ValueError

def stats_text(txt,count):
    stats_text_en(txt,count)
    stats_text_cn(txt,count)
