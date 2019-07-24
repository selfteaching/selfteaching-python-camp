from collections import Counter 
#提供了哈希对象的计算功能
import jieba
#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple jieba

# 封装统计英文单词词频的函数
def stats_text_en(text,count):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        # 用 str 类型的 isascii 方法判断是否是英文单词
        if len(element) and element.isascii:
            words.append(element)
    return Counter(words).most_common(count)       


# 统计参数中每个中文汉字出现的次数
def stats_text_cn(text,count):
    words = jieba.cut(text)
    tmp =[]
    for i in words:
        if len (i) > 1:
            tmp.append(i)
    return Counter(tmp).most_common(count)   


def stats_text(text,count):
    if type(text)!=str:
        raise ValueError('参数必须是 str 类型,输入类型 %s' % type(text))
    '''
    合并 英文词频 和 中文词频 的结果
    '''
    return stats_text_en(text,count) + stats_text_cn(text,count)


