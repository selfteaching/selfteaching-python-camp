# encoding=utf-8   在Python源码的头文件中要声明编码方式
import operator 
import re
from collections import Counter
import jieba

def stats_text_cn(text,count): 
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型，输入类型%s'%type(text))
    word_str = re.findall(r'[\w]',text)
    word_str = ''.join(word_str)
    word_list= jieba.cut(word_str) 
    
    my_list = []
    for e in word_list:                    
        if len(e) >= 2 and '\u4e00' <= e <= '\u9fff' :
            my_list.append(e)
    return Counter(my_list).most_common(count)


def stats_text_en(text,count):
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型，输入类型%s'%type(text))
    word_str = text.replace(','," ").replace('.'," ").replace('!'," ").replace('*'," ").replace('--'," ")
    word_str = re.sub(r'[^A-Za-z]',' ',word_str)
    word_list = word_str.split()
    return Counter(word_list).most_common(count)

def stats_text(text,count):
    if isinstance(text,str):
        raise ValueError('参数必须是 str 类型，输入类型%s' % type(text))
    return stats_text_en(text,count) + stats_text_cn(text,count)
