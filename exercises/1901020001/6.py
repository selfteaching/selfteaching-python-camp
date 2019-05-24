#统计参数中每个英文单位出现的次数
def starts_text_en(txt):
    elements = txt.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.raplace(symbol,'')
        if len(element):
            words.append(element)
    counter = {}
    word_set = set(words)
    for word in word_set:
        counter[word]=words.counter(word)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)


#统计参数中每个中文出现的次数
def starts_text_cn(text):
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    count = {}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = cn_character_set.count(character)
    return seted(counter.items(),key=lambda x:x[1],reverse=True)

en_text =