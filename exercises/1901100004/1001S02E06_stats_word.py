
def stats_text_en(text):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols：
            element = element.replace(symbols.'')
        if len(element):
            words.append(element)
    counter = {}
    word_set = set(words)

    for word in word_set:
        counter[word] = words.count(word)
    return sorted(counter.items(),key=lambda x: x[1],reverse=true)


    def stats_text_cn(text):
        cn_characters = []
        for characters in text:
            if '\u4e00' <= characters <= '\u9fff':
                cn_characters.append(characters)
        counter = {}
        cn_character_set = set(cn_characters)
        for character in cn_character_set:
            counter[character] = cn_characters.count(character)
        return sorted(counter.items(),key=lambda x: x[1], reverse=True)


        en_text =