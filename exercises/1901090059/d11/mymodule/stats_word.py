# 导入相应的 库 以供程序使用
# encoding=utf-8
import jieba
import re
from collections import Counter

# 1. 定义一个 stats_text_en 函数，统计输入给函数一个字符串中的所有的不同的英文单词的个数并按照从大到小排序

def stats_text_en (text_in, count):
    #提示输入一串字符串后，系统将统计其中英文单词个数并按照出现的频度进行排序。
    patternEn = re.compile( "[A-Z]*[a-z]+")

    if type(text_in)!= str:
        raise ValueError('非字符串类型')

    word_list = re.findall(patternEn,text_in)

    #采用 标准库中的 counter 进行排序
    return dict(Counter(word_list).most_common(count))

# 1. 定义一个 stats_text_cn 函数，统计输入给函数一个字符串中的所有的不同的中文汉字的个数
# 并按照出现的频度从大到小排序

def stats_text_cn (textIn, count):
    #提示输入一串字符串后，系统将统计其中包括中文汉字个数并按照出现的频度进行排序

    patternCn = re.compile("[\u4E00-\u9FFF]+")
    patternEn = re.compile( "[A-Z]*[a-z]+")

    if type(textIn)!= str:
        raise ValueError('非字符串类型')

    # 进行分词,并用空格进行联接
    seg_list = " ".join(jieba.cut(textIn, cut_all=False))

    # 分别取出其中的中文和英文 list
    new_list1 = re.findall(patternCn,seg_list)
    word_list2 = re.findall(patternEn,seg_list)

    #定义一个新的 list 类型变量，存储处理过的大于2的中文词
    words = []

    for element in new_list1:
        #提取分词后大于2的中文词存入字典
        if len(element) >= 2:
            words.append(element)

    # 将中文和英文的 List 相加组合
    word = words + word_list2

    # 返回 词频前 count 个数的 词及相应的词频
    return dict(Counter(word).most_common(count))

def stats_text(text_en_cn, count = 3):
    # 通过调用分别汉字和英文统计词频的两个函数并返回最终的统计结果，并进行合并并重新进行汉字英文词频混合排序

    if type(text_en_cn)!= str:
        raise ValueError('非字符串类型')
     
    # 调用英文词频统计 函数 stats_text_en 将结果存入 临时字典 dictTmpEn
    dictTmpEn = stats_text_en(text_en_cn, count)

    # 调用汉字词频统计 函数 stats_text_cn 将结果存入 临时字典 dictTmpCn
    dictTmpCn = stats_text_cn(text_en_cn, count)

    # 合并 汉字、英文丙个 dict 类型 数据 为一个字典 dictEnCn
    dictEnCn = dict(dictTmpEn, **dictTmpCn)
    
    #按照出现次数从大到小输出所有的汉字及出现次数,并返回
    dic_new = Counter(dictEnCn).most_common(count*2)
    return dic_new