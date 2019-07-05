import re
from collections import Counter

def stats_text_en(text):
    try:
        text + ''
    except:
        raise ValueError("oops, this is not a string!")
    else:
        word_list = re.findall(r'\b[a-z]+\'?[a-z]+',text.lower())
        count_dict = {}
        for word in word_list:
            count_dict[word] = word_list.count(word)
        list_en = Counter(word_list).most_common(10)
        return list_en

def stats_text_cn(text):
    try:
        text + ''
    except:
        raise ValueError("oops, this is not a string!")
    else:
        text_cn = re.sub(r'[\Wa-zA-Z0-9]','',text)
        count_dict = {}
        for char in text_cn:
            count_dict[char] = text_cn.count(char)
        list_cn = Counter(text_cn).most_common(100)
        return list_cn