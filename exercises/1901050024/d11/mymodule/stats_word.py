import collections
import re
import jieba
import string
def stats_word_en(en,count1):
    if isinstance(en,str):
        text1 = re.sub("[^A-Za-z]"," ",en.strip(string.punctuation))
        text1 = text1.lower()
        text1_list = text1.split()
        return collections.Counter(text1_list).most_common(count1)
    else:
        raise ValueError('请输入文本')
      
def stats_word_cn(cn,count2):
    if isinstance(cn,str):
        text2 = re.sub("[A-Za-z]"," ",cn)
        seg_list = jieba.cut(text2,cut_all=False)
        cn_list = []
        for i in seg_list:
            if len(i) >= 2:
                cn_list.append(i)
            else:
                pass
        return collections.Counter(cn_list).most_common(count2)    
    else:
        raise ValueError('请输入文本!')
        
def stats_word(text_en_cn,count_x):
    return stats_word_cn(text_en_cn,count_x)+stats_word_cn(text_en_cn,count_x)