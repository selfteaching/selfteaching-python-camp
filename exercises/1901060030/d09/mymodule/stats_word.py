import collections
import re

def stats_text_en(en_text, count):
    en_text = ascii(en_text)
    en_text = en_text.split(' ')
    en_text_f = []
    for i in en_text:
        en_text_f.append(i.lower())
    return collections.Counter(en_text_f).most_common(count)

def stats_text_cn(cn_text,count):
    cn_text_n = []
    for i in cn_text:
        cn_text_n.append(ord(i))
    cn_text_f = []
    for i in cn_text_n:
        cn_text_f.append(chr(i))
    return collections.Counter(cn_text_f).most_common(count)

def stats_text(text,count):
    """
    Count the frequency of each element of an array for both Chinese and English
    : param text: the text to be counted
    """
    if type(text) == str:
        # Build a list contains Chinese characters only
        cn_text = []
        for i in text:
            if ord(i) > 255:
                cn_text.append(i)
        # Build a list contains English words only
        en_text = re.sub("[^A-Za-z]", " ", text.strip())
        return (stats_text_cn(cn_text,count),stats_text_en(en_text,count))
    else:
        raise TypeError

           
