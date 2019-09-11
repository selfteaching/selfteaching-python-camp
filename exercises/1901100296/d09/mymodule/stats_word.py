import collections

def stats_text_en(text,count) :
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
     # 使用标准库的Counter统计词频，并排序输出
    return collections.Counter(words).most_common(count)
# 封装统计汉字词频的函数
def stats_text_cn(text,count):
    if type(text)!=str:
        raise ValueError('输入类型 %s,参数必须是 str 类型'%type(text))
    # 挑拣汉字出来
    words=[]
    for word in text:
        if '\u4e00' <= word <= '\u9fff':
            words.append(word)
    # 使用标准库的Counter统计词频，并排序输出
    return collections.Counter(words).most_common(count)
    
# 统计英文和汉字的函数
def stats_text(text,count):
    if type(text)!=str:
        raise ValueError('输入类型 %s,参数必须是 str 类型'%type(text))
    return(stats_text_cn(text,count)+stats_text_en(text,count))


