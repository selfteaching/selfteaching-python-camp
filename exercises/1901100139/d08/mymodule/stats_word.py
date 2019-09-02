def stats_text_en(text):
    if not isinstance(text,str):
        raise ValueError('参数必须为str类型，输入类型为 %s' % type(text))
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)
    counter = {}
    word_set = set(words)
    
    for word in word_set:
        counter[word] = words.count(word)
    return sorted(counter.items(), key=lambda x: x[1],reverse=True)
# 英文数组


def stats_text_cn(text):
    if not isinstance(text,str):
        raise ValueError('参数必须为str类型，输入类型为 %s' % type(text))
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(), key=lambda x: x[1],reverse=True)
# 中文数组

def stats_text(text):
    '''
    合并中英词频的结果
    '''
    if not isinstance(text,str):
        raise ValueError('参数必须为str类型，输入类型为 %s' % type(text))    
    return stats_text_en(text) + stats_text_cn(text)