
import re
import jieba
from collections import Counter
counter=20
def stats_text_en(text, counter):

    if not isinstance(text, str):
        raise ValueError("I can only handle a string type text")

    # first removing "-", useless space, then changing all words into lower-case.
    text_p = text.replace("\-", " ").strip().lower()
    # don't forgeting the "\n", Otherwise it will bring some awkawk words
    i = re.compile("[^a-z \n]")
    text_en = i.sub("", text_p).split()
    
    # using Sounter to create a dictionary sorted by frequency
    sort_en = Counter(text_en).most_common(counter)
    return sort_en


def stats_text_cn(text, counter):

    if not isinstance(text, str):
        raise ValueError("I can only handle a string type text")

    # only chinese left and change into a list.
    text_cn = ""
    for t in text:
        if ord(t) > 256:#ASCII编码，去除英文及符号
            text_cn = text_cn + t
        else:
            text_cn = text_cn + "，"
    list_cn_word = ([x for x in jieba.cut(text_cn, cut_all=False) if len(x) >= 2])

    # using Sounter to create a dictionary sorted by frequency
    sort_cn = Counter(list_cn_word).most_common(counter)
    return sort_cn
    print(sort_cn)

def stats_text(text, counter):
    if not isinstance(text, str):
        raise ValueError("I can only handle a string type text")

    sort_en = stats_text_en(text, counter)
    sort_cn = stats_text_cn(text, counter)


    


