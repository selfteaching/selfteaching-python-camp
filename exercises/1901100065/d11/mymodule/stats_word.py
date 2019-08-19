#############################################
# 使用标准库中的 Counter 来完善中英文统计的排序功能，
# 使函数能够按照词频出现的次数有序输出
#############################################
from collections import Counter
import jieba

def stats_text_en(text, count):
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
            text_list.append(word.lower())

    return Counter(text_list).most_common(count)


def stats_text_cn(text, count):
    """
    统计参数中每个中文汉字出现的次数，返回一个按字频降序排列的数组
    """
    
    if not isinstance(text, str):
       raise ValueError('返回参数必须是 str 类型，输入类型 %s ' % type(text))

   
    # 使用jieba的精确分词对text进行分词
    words = jieba.cut(text, cut_all=False)
    tmp = []
    for i in words:
        # 用字符串长度大于1的方法过滤所有的标点和特殊字符以及单字
        if len(i) > 1:
            tmp.append(i)
    return Counter(tmp).most_common(count)
    

def stats_text(text, count):
    """分别调⽤stats_text_en , stats_text_cn ，输出合并词频统计结果。
    """
    if not isinstance(text, str):
       raise ValueError('返回参数必须是 str 类型，输入类型 %s ' % type(text))


    return stats_text_en(text, count) + stats_text_cn(text, count)
    




