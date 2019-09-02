#统计参数中每个英文单词出现的次数
def stats_text_en(text):
    elements = text.split()

    words = []
    symbols = ',.“-*!'

    for element in elements:
        for symbol in symbols:
            #replace返回新的字符串，因此必须要新的字符串
            element = element.replace(symbol,'')
        #将非空字符添加到列表中
        if len(element) :
            words.append(element)

    #初始化一个counter字典，用来存放单词出现的频次
    counter = {}

    #去重，减少迭代次数
    word_set = set(words)

    for word in word_set:
        counter[word] = words.count(word)

    #2.从小到大排序输出

    return sorted(counter.items(), key = lambda x:x[1],reverse=True)

#统计参数中每个中文字符出现的次数
def stats_text_cn(text):
    cn_characters = []
     
    for character in text:
        #unicode中中文字符的范围
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    
    #print('中文字符列表==>',cn_characters)

    counter = {}

    #减少迭代次数
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(),key = lambda x:x[1],reverse=True)

def stats_text(text):
    cn_text = text[:text.rfind('\u3002')+1]
    en_text = text[text.rfind('\u3002')+1:]
    #print('resule is ==>',**stats_text_cn(cn_text),**stats_text_en(en_text))
    cn_result = stats_text_cn(cn_text)
    en_result = stats_text_en(en_text)
#    print('cn_result==>',cn_result)
#    print('en_result==>',en_result)
    merged_result = cn_result+en_result
    return (merged_result)
















    
