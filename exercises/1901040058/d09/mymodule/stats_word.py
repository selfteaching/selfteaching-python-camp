import re
import collections

def stats_text_en(text):#定义函数，统计英文单词计数
    if not isinstance(text, str):
        raise ValueError('Please input str text.')
    word_list = re.findall('[A-Za-z]+', text) #提取字符串中的英文单词
    print(collections.Counter(word_list).most_common(int(100)))

def stats_text_cn(text): #定义函数，统计汉字计数
    if not isinstance(text, str):
        raise ValueError('Please input str text.')
    word_list = re.findall('[\u4e00-\u9fa5]', text)#提取字符串中的汉字
    print(collections.Counter(word_list).most_common(int(100)))