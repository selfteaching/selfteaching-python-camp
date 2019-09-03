import collections
import re
import jieba 

def stats_text_en(text, count):
    # Build a list contains English words only
    en_text = re.sub("[^A-Za-z]", " ", text.strip())
    en_text = ascii(en_text)
    en_text = en_text.split(' ')
    en_text_f = []
    for i in en_text:
        en_text_f.append(i.lower())
    return collections.Counter(en_text_f).most_common(count)

def stats_text_cn(text,count):
    # Build a list contains Chinese characters only
    result1 = re.findall(u'[\u4e00-\u9fff]+', text.strip())
    newString = ''.join(result1)
    # Perform Chinese segmentation
    seg_list = jieba.cut(newString, cut_all = False)
    cn_text_f = []
    for i in seg_list:
        if len(i) >= 2:
                cn_text_f.append(i)
    return collections.Counter(cn_text_f).most_common(count) 
        
def stats_text(text,count):
    """
    Count the frequency of each element of an array for both Chinese and English
    : param text: the text to be counted
    """
    if type(text) == str:
        return (stats_text_cn(text,count),stats_text_en(text,count))
    else:
        raise TypeError

           
