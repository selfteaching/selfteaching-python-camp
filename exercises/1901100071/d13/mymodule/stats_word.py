from collections import Counter
import jieba

# pip install -i pip install -i https://pypi.tuna.tsinghua.edu.cn/simple jieba


# 统计参数中每个英⽂单词出现的次数
def stats_text_en(text, Count):
    elements = text.split()
    words = []
    symbols = ".*!'-"
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol," ")
        # 用 str 类型 的 isascii 方法判断是否是英文单词
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(Count)

# 统计参数中每个中⽂汉字出现的次数
def stats_text_cn(text, Count):
    words = jieba.cut(text)
    tmp = []
    for i in words:
        if len(i) > 1:
            tmp.append(i)
    return Counter(tmp).most_common(Count)

def stats_text(text, Count):
    '''
    合并 英文词频 和 中文字频 的结果
    '''
    if not isinstance(text,str):
        raise ValueError("参数必须是 str 类型，输入类型%s" % type(text))
    return stats_text_en(text, Count) + stats_text_cn(text, Count)


