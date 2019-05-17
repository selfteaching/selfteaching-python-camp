text= '''                       
The Zen of Python, by Tim Peters
美丽 is better than 丑陋.
清楚 is better than 含糊.
简单 is better than 复杂.
复杂 is better than 难懂.
单一 is better than 嵌套.
稀疏 is better than 稠密.
今天是星期一
'''
import re  
import collections  
count=int()
def stats_text_en(text,count):
    if type(text)!=str:
        raise ValueError("文本为非字符串")
    text=re.sub('[^a-zA-Z]','',text.strip()) #表示所有非英文字母
    text=text.split()
    #print(collections.Counter(text).most_common(count))

import jieba #导入第三方库
def stats_text_cn(text,count):    #定义检索中文函数
    if type(text)!=str:
        raise ValueError("文本为非字符串")

    text=re.sub('[^\u4e00-\u9fa5]','',text) #[^\u4e00-\u9fa5]表示所有非中文
    text=jieba.lcut(text)  #精确切分中文，返回一个list
    text1=[]
    for i in text: #筛选长度大于等于2的词
        if len(i)>=2:
            text1.append(i)
    a=collections.Counter(text1).most_common(count)
    return a


def stats_word(text,count): #定义函数，实现统计汉字和英文单词出现次数
    if type(text)!=str:
        raise ValueError("文本为非字符串")
    stats_text_en(text,count)
    stats_text_cn(text,count)

