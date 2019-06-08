# 统计参数中每个英文单位出现的次数
def stats_text_en(text):
    if not isinstance(text,str):
        raise ValueError
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol, '')
        if len(element)and element.isascii():
            words.append(element)
    counter = {}
    word_set = set(words)
    for word in word_set:
        counter[word]=words.count(word)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)


# 统计参数中每个中文出现的次数
def stats_text_cn(text):
    if not isinstance(text,str):
        raise ValueError
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)



def stats_text(text):
    if not isinstance(text,str):
        raise ValueError
#合并英文词频和中文字频的结果
    return stats_text_en(text)+stats_text_cn(text)