# 定义⼀个名为 stats_text_en 的函数，函数接受⼀个字符串 text 作为参数
def stats_text_en(text):
    elements = text.split()
    words =[]
    symbols=',.*!_-'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol, '')
        #判断是否为英文单词
        if len(element) and element.isascii():
            words.append(element)
    counter = {}
    word_set = set(words)
    for word in word_set:
        counter[word] = words.count(word)
    return sorted(counter.items(), key=lambda x: x[1], reverse= True)


#定义⼀个名为 stats_text_cn 的函数，函数接受⼀个字符串 text 作为参数
def stats_text_cn(text):
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character]= cn_characters.count(character)
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)

def stats_text(text):
#合并英文词频和中文字频的结果
    return stats_text_en(text) + stats_text_cn(text)
