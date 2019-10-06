from collections import Counter
import jieba

#定义一个统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
def stats_text_en(text,count):
    elements = text.split()
    words =[]

    symbols = ',.!*-?'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)    
   

#定义一个统计参数中每个中文单词出现的次数，最后返回一个按词频降序排列的数组
def stats_text_cn(text,count):
    cn_elements = []
    words =jieba.cut(text)
    for cn_element in words:
        if '\u4e00' <= cn_element <= '\u9fef':
            cn_elements.append(cn_element) 
    return Counter(cn_elements).most_commom(count)


    
#输出合并词频统计
def stats_text(text,count):
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型 %s' %type(text))    
    return stats_text_en(text,count)+stats_text_cn(text,count)



