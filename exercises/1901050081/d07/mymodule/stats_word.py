#统计参数中每个英文单词出现的次数
def stats_text_en(text):
    elements=text.split()
    words=[]
    symbols=',.*-?!'
    for element in elements:
        for symbol in symbols:
            element=element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)
    counter={}
    word_set=set(words)

    for word in word_set:
        counter[word]=words.count(word)
    return sorted(counter.items(), key=lambda x:x[1], reverse=True)

#统计参数中每个中文汉字出现的次数
def stats_text_cn(text):
    cn_charactors=[]
    for charactor in text:
        if '\u4e00' <= charactor <= '\u9fff':
            cn_charactors.append(charactor)
    counter={}
    cn_charactor_set=set(cn_charactors)
    for charactor in cn_charactor_set:
        counter[charactor]=cn_charactors.count(charactor)
    return sorted(counter.items(), key=lambda x:x[1], reverse=True)

#统计英文单词和中文汉字的词频合计
def stats_text(text):
    return stats_text_en(text) + stats_text_cn(text)



if __name__ == '__main__':
    print()