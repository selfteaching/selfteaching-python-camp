
#统计参数中每个英文单词出现的次数，按词频降序排列数组
#对函数输入字符串进行分词，统计完成分词之后的词频，只统计长度大于等于2的词
# 思路：1、对输入字符串jieba.cut("需要分词的字符串", cut_all=False)（精确模式）
    #  2、for循环，len()  
import jieba
from collections import Counter

def stats_text_cn(text):

    if  not isinstance(text,str):
        raise TypeError('输入的不是文本格式')

    text = jieba.lcut(text,cut_all = False)#生成列表
    

    d = {}
    for x in text:
        if len(x) >=2 and u'\u4e00' <= x <= u'\u9fff' :
            d[x] = text.count(x)
    print(Counter(d).most_common(20))


with open('/Users/shining/Documents/GitHub/selfteaching-python-camp/19100302/7Lou/tang300.json','r',encoding='utf-16') as f:
    text = f.read()
    print(stats_text_cn(text))