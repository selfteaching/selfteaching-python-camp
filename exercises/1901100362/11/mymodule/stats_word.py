#统计参数中每个英文单词出现的次数
#encoding = utf-8
import string
from collections import Counter
import jieba


def stats_text_en(text,count):
    if not isinstance(text,str):
        raise ValueError("text参数必须是字符串 %s" % type(text))
    elif not isinstance(count,int):
        raise ValueError("count参数必须是int %d" % type(count))

    elements = text.split()
    words = []
    symbols = ',.*-!'

    for element in elements:
        for symbol in symbols:
            element.replace(symbol,' ')
        if len(element) and element.isascii():
            words.append(element)

    return Counter(words).most_common(count)

#统计参数中每个中文字符出现的次数
def stats_text_cn(text,count):
    
    if not isinstance(text,str):
        raise ValueError("参数必须是字符串 %s" % type(text))
    elif not isinstance(count,int):
        raise ValueError("count参数必须是int %d" % type(count))
    
#    s1 = ' '.join(seg_list))  # 精确模式

    cn_characters = []
    for character in text:
        if  '\u4e00'<=character<='\u9fff':
            cn_characters.append(character)
    s1 = ''.join(cn_characters)
    seg_list = [ element for element in jieba.cut(s1, cut_all=False) if len(element)>2] 
   
    return Counter(seg_list).most_common(count)
    
        

    


def stats_text(text,count):
    
    if not isinstance(text,str):
            raise ValueError("参数必须是字符串 %s" % type(text))
    elif not isinstance(count,int):
        raise ValueError("count参数必须是int %d" % type(count))

    return stats_text_cn(text,count) + stats_text_en(text,count)
















    
