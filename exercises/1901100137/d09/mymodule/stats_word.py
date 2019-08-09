from collections import Counter

#定义一个名为 stats_text_en的函数
def stats_text_en(text,count):
    #创建一个空白的文档以便储存整理过的单词
    words=[]
    #使用split（）去除非英文单词符号
    elements = text.split()
    symbols = ', . * !'
    for element in elements:
        for symbols in symbols:
            element =element.replace(symbols,'')
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)

#定义一个名为 stats_text_cn的函数
def stats_text_cn(text,count):
    cn_characters = []
    for character in text:
        # unicode 中 中文 字符的范围
        if '\u4e00' <= character <='\u9fff':
             cn_characters.append(character)
    return Counter(cn_characters).most_common(count)
    
#合并显示中文及英文字符数量
def stats_text(text,count):
    if not isinstance(text,str) :
        raise ValueError("text 必须是 str 类型")
    '''
    合并显示中文及英文字符数量
    '''
    return stats_text_en(text,count) + stats_text_cn(text,count)

