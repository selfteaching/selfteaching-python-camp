#统计参数中每个英文单词出现的次数
def stats_text_en(text):

    if not isinstance(text,str):
        raise ValueError('unexpected type')

    count=int(input('输出元素的个数： '))

    elements=text.split()
    words=[]
    symbols=',.*-?!'
    for element in elements:
        for symbol in symbols:
            element=element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)
    import collections
    counter=collections.Counter(words).most_common(count)
    return counter

#统计参数中每个中文汉字出现的次数
def stats_text_cn(text):
    
    if not isinstance(text,str):
        raise ValueError('unexpected type')

    count=int(input('输出元素的个数： '))

    cn_charactors=[]
    for charactor in text:
        if '\u4e00' <= charactor <= '\u9fff':
            cn_charactors.append(charactor)
    cn_words=''.join(cn_charactors)
    import jieba
    seg_list=jieba.cut(cn_words,cut_all=False)
    words_list=list(seg_list)
    words=[]
    for word in words_list:
        if len(word)>=2:
            words.append(word)
    import collections
    counter=collections.Counter(words).most_common(count)

    return counter


#统计英文单词和中文汉字的词频合计
def stats_text(text):

    if not isinstance(text,str):
        raise ValueError('unexpected type')
        
    return stats_text_en(text) + stats_text_cn(text)



if __name__ == '__main__':
    text='我爱中国天安门'
    print(stats_text_en(text))
    print(stats_text_cn(text))
    print(stats_text(text))