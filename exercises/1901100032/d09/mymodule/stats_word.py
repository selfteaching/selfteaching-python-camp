from collections import Counter

def stats_text_en(text, count):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)


def stats_text_cn(text, count):
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    return Counter(cn_characters).most_common(count)


def stats_text(text, count):
    '''
    '''
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型，输入类型 %s' % type(text))
    return stats_text_en(text,count) + stats_text_cn(text, count)
