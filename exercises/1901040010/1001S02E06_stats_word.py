text1 = '''
Beautiful is better than ugly.
Explicit is better than implicit.
'''

def stats_text_en(text1):
    elements = text1.split()                      #整理字符
    words = []                                    #给字符列表
    symbols = '*-,.'                              #清理文档中的符号
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')  #把整理好的字符不含符号的加入
        if len(element):                          #字符长度
            words.append(element)
    counter = {}                                  #建立字典
    word_set = set(words)                         #设置字符
    for word in word_set:
        counter[word] = words.count(word)         #清点次数
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)  #排序
if __name__ =='__main__':
    
    print('英文单词词频降序排列 \n', stats_text_en(text1))


text2 = '''
昨天下雨了，今天又下雨了，明天还会下雨吗？
'''

def stats_text_cn(text2):
    characters = []                               #给字符列表
    for character in text2:
        if '\u4e00'<=character<='\u9fff':         #检查是否为中文字符
            characters.append(character)
    counter = {}                                  #建立字典
    characters_set = set(characters)              #设置字符
    for character in characters_set:
        counter[character] = characters.count(character)   #清点次数
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)  #排序
if __name__=='__main__':
    print('中文汉字字频降序排列 \n', stats_text_cn(text2))
