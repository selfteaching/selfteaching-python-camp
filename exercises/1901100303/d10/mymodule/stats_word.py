
from collections import Counter
import jieba

########## 1.统计英文词频
def stats_text_en(text,count):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
            #用 str 类型的 isascii 方法 判断是否是英文单词
            if len(element) and element.isascii():
                words.append(element)
    return Counter(words).most_common(count)


######################   2.输出中文函数
def stats_text_cn(text,count):
    words = jieba.cut(text)
    tmp =[]
    for i in words:
        if len(i) > 1:
            tmp.append(i)
    return Counter(tmp).most_common(count)
    

         
   
def stas_text(text,count):
    '''
    合并英文词频 和 中文词频
    '''
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型，输入类型 %s' % type(text))
    return stats_text_cn(text,count) + stats_text_en(text,count)






