from collections import Counter
import jieba

# 创建一个函数，统计参数中每个英文单词词频
def stats_text_en(text,count):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        # 用 str 类型的 isascii 方法判断是否是英文单词
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)


#定义一个函数,统计参数中每个中文汉字出现的次数
def stats_text_cn(text,count):
    characters_cn = []
    characters_1 = jieba.cut(text,cut_all=False)
    for character in characters_1:
        if len(character) >= 2:
            characters_cn.append(character)
    return Counter(characters_cn).most_common(count)


# 创建一个函数，分别调用stats_text_en和stats_text_cn
def stats_text(text,count):
    """
    分别调用stats_word_en和stats_text_cn函数，输出合并词频统计结果
    """
    if not isinstance(text,str):
        raise ValueError('输入参数必须为str类型，当前输入类型为%s'%type(text))
    return stats_text_en(text,count) + stats_text_cn(text,count)
