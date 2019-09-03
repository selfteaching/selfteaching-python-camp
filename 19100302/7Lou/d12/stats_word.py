#统计参数中每个英文单词出现的次数，按词频降序排列数组
from collections import Counter

def stats_text_en(text):
    if  not isinstance(text,str):
        raise TypeError('输入的不是文本格式')
    text = text.replace("\n"," ").replace(","," ").replace("."," ").replace("*"," ").replace("--"," ")
    print(Counter(text.split()).most_common())

#统计参数中每个汉字单词出现的次数，按字频降序排列数组

'''def stats_text_cn(text):
    if  not isinstance(text,str):
        raise TypeError('输入的不是文本格式')
    d = {}
    for x in text:
        if u'\u4e00' <= x <= u'\u9fff' :
            d[x] = text.count(x)
    print(Counter(d).most_common())'''

#统计参数中每个英文单词出现的次数，按词频降序排列数组
#对函数输入字符串进行分词，统计完成分词之后的词频，只统计长度大于等于2的词
# 思路：1、对输入字符串jieba.cut("需要分词的字符串", cut_all=False)（精确模式）
    #  2、for循环，len()  
import jieba
from collections import Counter

def stats_text_cn(text):
    i=int (input("英文词频最高的前i个词，请输入i："))

    if  not isinstance(text,str):
        raise TypeError('输入的不是文本格式')

    text = jieba.lcut(text,cut_all = False)#生成列表
    

    d = {}
    for x in text:
        if len(x) >=2 and u'\u4e00' <= x <= u'\u9fff' :
            d[x] = text.count(x)
        
    print(Counter(d).most_common(i))

    
#分别调用stats_text_en , stats_text_cn 合并输出词频统计结果
def stats_text(text):
    
        stats_text_cn(text)
        stats_text_en(text)


