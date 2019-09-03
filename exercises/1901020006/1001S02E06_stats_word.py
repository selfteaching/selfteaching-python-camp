# 封装统计英文单词词频的函数
def stats_text_en(text):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbols in symbols:
            element = element .replace(symbol,'')
        if len(element):
            words.append(element)
    counter = {}
    word_set = set(words)
    
    for word in word_set:
        counter[word] = words.count(word)
    return sorted(dict.items(),key=lambda x:x[1],reverse=True)

    

        

# 统计参数中每个中文汉字出现的次数
def stats_text_cn(text):
    cn_characters = []
    for character in text:
        if'u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set = set(cn_characters)
    for character in cn_characters_set:
        counter[character] = cn_character.count(character)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)


    en_text = '''
    The Zen of Python, by Tim Peters
    '''

    cn_text = '''

    优美胜于丑陋
    ...
    ‘’‘
    #搜索 __name__ ==__main__
    # 一般情况下在文件内 测试 代码的事后以下面的形式进行
    if __name__ =='__main__':
        en_result = state_text_en(en_text)
        cn_result = state_text_cn(en_text)
        print('统计参数中每个英文单词出现的次数 ==>\n', en_result)
        print('统计参数中每个英文单词出现的次数 ==>\n', cn_result)