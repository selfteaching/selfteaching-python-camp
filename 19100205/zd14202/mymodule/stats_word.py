#这是一个单独统计英文单词和单独统计中文单字以及统计中文字和英文词词频（字频）

import re
import collections
import jieba 

count = int()

"""创建一个名为stats_text_en的函数，它的功能是为统计英文词频"""
def stats_text_en(text,count):
    '''判断输入的是字符，执行以下语句'''
    if type(text) == str :   
        '''只保留字母，并用空格作为分隔符'''
        text_en = re.sub("[^A-Za-z]", " ", text.strip())   
        '''以空格以及折行为分隔，将每个被分割的内容作为一个列表元素，并将所有列表元素合在一起组成一个列表'''
        list_en = text_en.split( )   
        '''利用colections中的Counter为list_en中的每个出现的英文单词计数，返回前count个词频最高的词及出现的次数'''
        return collections.Counter(list_en).most_common(count)   
    else: 
	    raise ValueError ('输入的类型不为字符串')   

"""创建一个名为stats_text_cn的函数，它的功能是为统计中文词频"""
def stats_text_cn(text,count) :
    '''判断输入的是字符，执行以下语句'''
    if type(text) == str : 
        '''保留所有匹配的汉字Unicode码的字符'''
        list_cn = re.findall(u'[\u4e00-\u9fff]+', text.strip())
        '''将list_en不用任何分隔符连接起来'''
        str_cn = ''.join(list_cn)
        '''day_10作业：通过jieba的精确模式将字符串str_cn进行分词,只要前长度大于2的词'''
        seg_list =[ x for x in jieba.cut_for_search(str_cn) if len(x) >= 2]

        '''利用colections中的Counter为list_cn中的每个出现的英文单词计数，返回前count个词频最高的词及出现的次数'''
        return collections.Counter(seg_list).most_common(count)
    else :
	    raise ValueError ('输入的类型不为字符串')

"""创建一个名为stats_text的函数，它的功能是为统计中文字和英文词频,并返回词频最高的前count个单词"""
def stats_text(text,count):
    '''利用colections中的Counter为list1中的每个出现的英文单词计数，
    并利用collections.OrderedDict将stats_text_en(text)和stats_text_cn(text)的返回结果合二为一，
    返回前count个词频最高的词及出现的次数（其中max表示返回所有汉字和英文字的词频）'''
    return collections.OrderedDict(collections.Counter(stats_text_en(text,max)+stats_text_cn(text,max)).most_common(count))