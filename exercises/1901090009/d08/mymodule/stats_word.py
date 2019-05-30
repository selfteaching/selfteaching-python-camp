import re

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
        list_en = sorted(count_dict.items(), key = lambda X: X[1], reverse=True)
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
        list_cn = sorted(count_dict.items(), key = lambda x: x[1], reverse=True)
        return list_cn

def stats_text(text):
    list_en = stats_text_en(text)
    list_cn = stats_text_cn(text)
    list_all = sorted((list_en + list_cn), key = lambda x: x[1], reverse=True)
    return list_all