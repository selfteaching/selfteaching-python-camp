from collections import Counter


#统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
def stats_text_en(text,count):
    if not isinstance(text,str):
        raise ValueError("参数必须是str类型，输出类型%s"%type(text))
    liebiao=text.split()
    a=[]
    symbols='.-*!,'
    for b in liebiao:
        for symbol in symbols:
            b=b.replace(symbol,'')
        if len(b) and b.isascii():
           a.append(b)
    return Counter(a).most_common(count)    


#统计参数中每个中文汉字出现的次数
def stats_text_cn(text,count):
    if not isinstance(text,str):
        raise ValueError("参数必须是str类型，输出类型%s"%type(text))
    text_character=[]
    for character in text:
        if '\u4e00'<=character<='\u9fff':
            text_character.append(character)
    return Counter(text_character).most_common(count)
    

en_text='''
asada afaff wffa, agrwe.
gssdhc -- *yfhsdhci*, frdcsc!
gssdhc gssdhc asada
'''

cn_text='''
自学训练营
练练练
学学
'''

#输出合并词汇统计结果
def stats_text(text,count):
    if not isinstance(text,str):
        raise ValueError("参数必须是str类型，输出类型%s"%type(text))
    return stats_text_cn(text,count) + stats_text_en(text,count)

