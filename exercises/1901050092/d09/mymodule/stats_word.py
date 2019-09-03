from collections import Counter

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


def  stats_text_cn(text,count):
    '''封装统计中文汉字字频的函数'''
    if not isinstance(text, str):
        raise ValueError('参数为非字符串')
    cn_charaters=[]
    symbols=', . *-!，。  '
    for charater in text:
        for symbol in symbols:
            charater=charater.replace(symbol,'')
        if '\u4e00 <=charater <=u9fff':
            cn_charaters.append(charater)

    return Counter(cn_charaters).most_common(count)



def stats_text(text,count):
    '''
    合并中，英文词频的结果
    '''
    if not isinstance(text, str):
        raise ValueError('参数为非字符串')
        
    return stats_text_en(text,count) + stats_text_cn(text,count)


