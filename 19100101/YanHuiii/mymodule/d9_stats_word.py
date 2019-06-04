#这是一个单独统计英文单词和单独统计中文单字以及统计中文字和英文词词频（字频）

import re
import collections

dict1 = {}
dict2 = {}
str1 = ''
count = int()

"""创建一个名为stats_text_en的函数，它的功能是为统计英文词频"""
def stats_text_en(text):
    
    '''只保留英文'''
    text = re.sub("[^A-Za-z]", " ", text.strip())
    '''将字符串text转换为列表list1,只保留单词为list1中的元素'''
    list1 = re.split(r"\W+",text)   
    '''删除list1中为空的列表元素'''
    while '' in list1:   
        list1.remove('')
    
    '''利用colections中的Counter为list1中的每个出现的英文单词计数，并以字典的形式返回'''
    return collections.Counter(list1)


'''创建一个名为stats_text_cn的函数，并用它实现统计汉字词频的功能'''


"""创建一个名为stats_text_cn的函数，它的功能是为统计中文词频"""
def stats_text_cn(text):
    
    """去掉text中的英文和数字"""
    text = re.sub("[A-Za-z0-9]", "", text)
    '''将字符串text转换为列表list1,只保留单词为list1中的元素'''
    list1 = re.split(r"\W+",text)   

    '''删除list1中为空的列表元素'''
    while '' in list1:   
        list1.remove('')
    
    str1 = ''.join(list1)
    
    return collections.Counter(str1)

#第九天的代码
"""创建一个名为stats_text_count的函数，它的功能是为统计中文字和英文词频,并返回词频最高的前count个单词"""

def stats_text_count(text,count):
    '''利用colections中的Counter为list1中的每个出现的英文单词计数，并利用collections.OrderedDict将stats_text_en(text)和stats_text_cn(text)的返回结果合二为一，返回前count个词频最高的词及出现的次数'''
    return collections.OrderedDict(collections.Counter(stats_text_en(text)+stats_text_cn(text)).most_common(count))

"""创建一个名为stats_text_en_count的函数，它的功能是为统计英文词频,并返回词频最高的前count个单词"""
def stats_text_en_count(text,count):
    
    '''只保留英文'''
    text = re.sub("[^A-Za-z]", " ", text.strip())
    '''将字符串text转换为列表list1,只保留单词为list1中的元素'''
    list1 = re.split(r"\W+",text)   
    '''删除list1中为空的列表元素'''
    while '' in list1:   
        list1.remove('')
    
    '''利用colections中的Counter为list1中的每个出现的英文单词计数，返回前count个词频最高的词及出现的次数'''
    return collections.Counter(list1).most_common(count)

"""创建一个名为stats_text_cn_count的函数，它的功能是为统计中文字频,并打印字频最高的前count个单词"""
def stats_text_cn_count(text,count):
    
    """去掉text中的英文和数字"""
    text = re.sub("[A-Za-z0-9]", "", text)
    '''将字符串text转换为列表list1,只保留单词为list1中的元素'''
    list1 = re.split(r"\W+",text)   

    '''删除list1中为空的列表元素'''
    while '' in list1:   
        list1.remove('')
    
    str1 = ''.join(list1)
    
    '''利用colections中的Counter为list1中的每个出现的英文单词计数，返回前count个字频最高的字及出现的次数'''
    return collections.Counter(str1).most_common(count)