import re
from collections import Counter
import jieba

def stats_text_en(text,count):
    '''统计字符串里每个英文单词的词频，返回按照词频降序排列的数组'''
    
    #字符串类型监测
    if type(text) == str:
        #提取字符串里的英文单词
        word_list = re.findall('[A-Za-z]+', text)
        #统计词频
        result = Counter(word_list).most_common(count)
        return result
    else:
        raise ValueError(f'传入的是{type(text)}类型,请传入字符串')



def stats_text_cn(text,count):
    '''统计字符串里每个汉字的词频，返回按照词频降序排列的数组'''

    #字符串类型监测
    if type(text) == str:
        #提取字符串里的中文汉字
        word_list = re.findall('[\u4e00-\u9fa5]+', text)
        word_str = ','.join(word_list)
        #使用jieba分词
        word_generator = jieba.cut(word_str)
        word_list_1 = [word for word in word_generator if len(word)>=2]
        #统计词频
        result = Counter(word_list_1).most_common(20)
        return result
    else:
        raise ValueError(f'传入的是{type(text)}类型,请传入字符串')


def stats_text(text,count):
    '''分别调⽤stats_text_en , stats_text_cn ，输出合并词频统计结果'''
    
    #字符串类型监测
    if type(text) == str:
        result = stats_text_en(text,count) + stats_text_cn(text, count)
        return result
    else:
        raise ValueError(f'传入的是{type(text)}类型,请传入字符串')