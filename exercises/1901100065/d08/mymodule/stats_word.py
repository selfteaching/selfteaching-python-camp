def stats_text_en(text):
    """输入一个英文字符串，统计字符串种每个英文但此出现的次数，最后返回一个按词频降序排列的数组。
    """

    if not isinstance(text, str):
       raise ValueError('返回参数必须是 str 类型，输入类型 %s ' % type(text))

    # 将输入的字符串分词并整理成小写单词的列表
    text1 = text.split()
    text_list = []
    symbols = '!,.-!*\''
    for word in text1:
        for symbol in symbols:
            word.replace(symbol,'')
        if len(word) and word.isascii():
            text_list.append(word)

    # 根据将整理好的列表统计每个单词出现的次数，用字典存储
    word_dict = {}
    for word in text_list:
        if word in word_dict.keys():
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict.update({word:1})
    
    # 返回降序排列的单词列表
    words = sorted(word_dict.items(), key=lambda x:x[1], reverse = True)
    return words


def stats_text_cn(text):
    """
    统计参数中每个中文汉字出现的次数，返回一个按字频降序排列的数组
    """
    
    if not isinstance(text, str):
       raise ValueError('返回参数必须是 str 类型，输入类型 %s ' % type(text))


    # 将字符串变成一个单个中文字组成的列表
    text_list = [word for word in text if '\u4e00' <= word <= '\u9fff']
    
    # 生成记录每个中文字出现次数的字典
    counter = {}
    cn_set = set(text_list)
    for word in cn_set:
        counter[word] = text_list.count(word)
    
    words = sorted(counter.items(), key=lambda x:x[1], reverse = True)
    return words
    

def stats_text(text):
    """分别调⽤stats_text_en , stats_text_cn ，输出合并词频统计结果。
    """
    if not isinstance(text, str):
       raise ValueError('返回参数必须是 str 类型，输入类型 %s ' % type(text))


    return stats_text_en(text) + stats_text_cn(text)
    




