from collections import Counter
import jieba
# 统计参数中每个英文单位出现的次数
def stats_text_en(text,count):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol, '')
        if len(element)and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)


# 统计参数中每个中文出现的次数
def stats_text_cn(text,count):
    words = jieba.cut(text)
    cn_characters = []
    for character in words:
        if len(character)> 1:
            cn_characters.append(character)
    return Counter(cn_characters).most_common(count)


def stats_text(text,count):
    if not isinstance(text,str):
        raise ValueError('参数必须是类型，输入类型%s' % type(text))
    return stats_text_en(text,count)+stats_text_cn(text,count)