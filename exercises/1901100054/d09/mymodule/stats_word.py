from collections import Counter

# 封装统计英⽂单词词频的函数
def stats_text_en(text,count):
    elements = text.split()
    words = []
    symbols = ',.*-!'

    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)

    return Counter(words).most_common(count)


# 统计参数中每个中⽂汉字出现的次数
def stats_text_cn(text,count):
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    return Counter(cn_characters).most_common(count)


def stats_text(text, count):  # 合并英文词频和中文字频的结果
    if not isinstance(text, str):
        raise ValueError('参数必须是 str 类型，输入类型 %s' % type(text))
    return stats_text_en(text, count) + stats_text_cn(text, count)

