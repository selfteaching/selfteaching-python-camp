# 封装统计英文单词词频的函数
def stats_text_en(text) :
    # if type(text)!=str:
    if not isinstance(text,str):
        raise ValueError('输入类型 %s,参数必须是 str 类型'%type(text))
    list_text=text.lower().split()
    words=[]
    #剔除特殊字符并删除空字符
    symbols='*--?!.,:，、。「」'
    for word in list_text:
        for symbol in symbols:
            word=word.replace(symbol,'')
            if len(word) and word.isascii():
                words.append(word)
        # 使用字典类型统计文本中单词数
    word_dic={}
    keys_set=set(words)
    for word in keys_set:
        word_dic[word]=words.count(word)  
    # 对字典的值降序排列
    return sorted (word_dic.items(),key=lambda item:item[1],reverse=True)
    
# 封装统计汉字词频的函数
def stats_text_cn(text):
    if type(text)!=str:
        raise ValueError('输入类型 %s,参数必须是 str 类型'%type(text))
    # 挑拣汉字出来
    words=[]
    for word in text:
        if '\u4e00' <= word <= '\u9fff':
            words.append(word)
        # 统计文本中汉字个数
    word_dic={}
    keys_set=set(words)
    for word in keys_set:
        word_dic[word]=words.count(word)
    # 对字典值降序排列
    return sorted (word_dic.items(),key=lambda item:item[1],reverse=True)
    
# 统计英文和汉字的函数
def stats_text(text):
    if type(text)!=str:
        raise ValueError('输入类型 %s,参数必须是 str 类型'%type(text))
    return(stats_text_cn(text)+stats_text_en(text))
