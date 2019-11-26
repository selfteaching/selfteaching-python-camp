import re

def stats_text_en(text):#定义函数，统计英文单词计数
    if not isinstance(text, str):
        raise ValueError('Please input str text.')
    word_list = re.findall('[A-Za-z]+', text) #提取字符串中的英文单词
    word_dict={word:word_list.count(word) for word in word_list}#创建英文单词计数字典
    dict1=sorted(word_dict.items(), key=lambda d:d[1], reverse = True)#按照值降序排序
    return dict1

def stats_text_cn(text): #定义函数，统计汉字计数
    if not isinstance(text, str):
        raise ValueError('Please input str text.')
    word_list = re.findall('[\u4e00-\u9fa5]', text)#提取字符串中的汉字
    word_dict={word:word_list.count(word) for word in word_list}#创建汉字计数字典
    dict1=sorted(word_dict.items(), key=lambda d:d[1], reverse = True)#按照值降序排序
    return dict1

def stats_text(text): #定义函数，分别调⽤stats_text_en , stats_text_cn ，输出合并词频统计结果
    if not isinstance(text, str):
        raise ValueError('Please input str text.')
    result = stats_text_en(text) + stats_text_cn(text)
    return result