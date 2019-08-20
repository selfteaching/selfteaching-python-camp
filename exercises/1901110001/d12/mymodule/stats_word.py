from collections import Counter
import jieba
import request



def stats_text_en(text,count):
    if not isinstance(text, str):
        raise ValueError('参数应当为str类型')
    a=text.split()
    symbols='。，；--*'
    words=[]
    for a1 in a:
        for symbol in symbols:
            b=a1.replace(symbol,'')
            words.append(b)
    return Counter(words).most_common(count)

def stats_text_cn(text, count):
    words = jieba.cut(text)
    x = []
    for word in words:
        if len(word) > 1:
            x.append(word)
    for i in words:
        if len(i) > 1:
            x.append(i)
    return Counter(x).most_common(count)
        
def stats_text(text,count):
    if not isinstance(text,str):
        raise ValueError('参数必须为str类型')
    return stats_text_cn(text,count) + stats_text_en(text,count)