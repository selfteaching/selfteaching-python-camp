from collections import Counter
import jieba

def  stats_text_en(text,count):
    '''封装统计英文单词词频的函数'''
    if not isinstance(text, str):
        raise ValueError('参数为非字符串')    
    elements=text.split()
    words=[]
    symbols=' ,  .*-!'
    for element in elements:
        for symbol in symbols:
            element=element.replace(symbol,'')
        if len(element)and element.isascii():
            words.append(element)

    return Counter(words).most_common(count)


def stats_text_cn(text,count):
    '''封装统计中文汉字字频的函数'''
    
    words = jieba.cut(text)
    tmp = []
    for i in words:
        if len(i) > 1:
            tmp.append(i)    
    return Counter(tmp).most_common(count)



def stats_text(text,count):
    '''
    合并中，英文词频的结果
    '''
    if not isinstance(text, str):
        raise ValueError('参数为非字符串')
        
    return stats_text_en(text,count) + stats_text_cn(text,count)


