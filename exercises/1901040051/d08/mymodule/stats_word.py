text = 12

# text = []

import collections
import re

def stats_text_en(string_en):
    if type(string_en)!= str:   
        raise ValueError('文本为非字符串')
    result = re.sub("[^A-Za-z]", " ", string_en.strip())
    newList = result.split( )
    print('英文单词词频统计结果： ',collections.Counter(newList),'\n')
    

def stats_text_cn(string_cn):
    if type(string_cn)!= str:   
        raise ValueError('文本为非字符串')
    result1 = re.findall('[\u4e00-\u9fff]+', string_cn)
    newString = ''.join(result1)
    print('中文单词词频统计结果： ',collections.Counter(newString),'\n')


# 调用函数
# stats_text_en(text)
# stats_text_cn(text)

def stats_text(text):  # 合并中英文词频统计, 如何调用两个函数 【原来就是两个函数相加这么简单。】

        """combine the stats_text_cn and stats_text_en,count english words and chinese characters"""
        if type(text) != str:   
            raise ValueError('文本为非字符串')
        a = stats_text_en(text)

        b = stats_text_cn(text)

        c = a+b

stats_text(text)

# import stats_word

