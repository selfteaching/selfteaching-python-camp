import collections
import re

def stats_text_en(text):
    """
    函数 stats_text_en(text) 的功能: 统计字符串 text 里的各个英文单词出现的次数, 按降序排列

    函数的返回结果 en_counter_sort 是 list 类型, 它的元素是 tuple 类型, 
    这里的 tuple 的元素包含一个字符串（单词）和一个数字（出现的次数）, 例如('good', 10)
    """

    # 参数类型检查, 如果输⼊参数不为字符串类型则抛出 ValueError 错误, 并包含完整的错误提示信息
    if type(text) != str:
        raise ValueError("您输入的是非字符串类型") 
    
    # if not isinstance(text, str): 
	#     raise ValueError("您输入的是非字符串类型" % type(text))

    text = text.lower()
    count = 100
    en = re.sub( r'[^A-Za-z]', ' ', text ) # 只取英文单词
    words = en.split()
    en_counter_sort = collections.Counter(words).most_common(count)
    return en_counter_sort


def stats_text_cn(text):
    """
    函数 stats_text_cn 的功能: 统计字符串 text 里的每个汉字出现的次数, 按降序排列

    函数的返回结果 cn_counter_sort 是 list 类型, 它的元素是 tuple 类型, 
    这里的 tuple 的元素包含一个字符串（汉字）和一个数字（出现的次数）, 例如('好', 10)
    """

    # 参数类型检查, 如果输⼊参数不为字符串类型则抛出 ValueError 错误, 并包含完整的错误提示信息
    if type(text) != str:
        raise ValueError("您输入的是非字符串类型") 
    
    # 不像英文单词是一串字母, 汉字本身就单个的
    # 根据 unicode 里中文字符的范围, 将 text 里的所有汉字挑出来
    count = 100
    words = re.findall( r'[\u4e00-\u9fa5]', text ) # 中文的Unicode编码范围为：[\u4e00-\u9fa5]
    cn_counter_sort = collections.Counter(words).most_common(count)
    return cn_counter_sort


def stats_text(text):
    """
    函数 stats_text(text) 的功能: 分别调⽤ stats_text_en, stats_text_cn, 输出合并词频统计结果
    """
    
    # 参数类型检查, 如果输⼊参数不为字符串类型则抛出 ValueError 错误, 并包含完整的错误提示信息
    if type(text) != str:
        raise ValueError("您输入的是非字符串类型") 
    
    word_counter = stats_text_en(text) + stats_text_cn( text )
    return word_counter