import jieba
import collections
import re
import string
top_n = int()
def stats_text_en(text, top_n = None):
    if isinstance(text, str): #判断是否为字符串
        pass
    else:
        raise ValueError('非字符串，请重新输入。Not a string, please type again')
    text = re.sub("[^A-Za-z]"," ",text.strip(string.punctuation))
    text1 = text.lower()
    text_list = text1.split()
    return collections.Counter(text_list).most_common(top_n)
 

def stats_text_cn(text, top_n = None):
    if isinstance(text, str):
        pass
    else:
        raise ValueError('非字符串，请重新输入。Not a string, please type again')        
    text1 = re.sub(r'[a-zA-Z0-9]','',text)
    seg_list = jieba.cut(text1)
    word_cn2 = [word_cn for word_cn in seg_list if len(word_cn) > 1]
    return collections.Counter(word_cn2).most_common(top_n) 
    
def stats_text(text,top_n = None):
    if isinstance(text, str):
        pass
    else:
        raise TypeError
    return stats_text_en(text, top_n) + stats_text_cn(text, top_n)

