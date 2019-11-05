# encoding=utf-8
import jieba
from collections import Counter

def stats_text_en(text, counter_sum): #封装统计英⽂文单词词频的函数
    if not isinstance(text,str): 
        raise ValueError ("please input string type!") 
    if not isinstance(counter_sum,int): 
        raise ValueError ("please input int type!")
    text=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
    text=text.split()
    dict_test={}
    counter_sum = int(counter_sum)
    for i in text:  
        count=text.count(i)
        r1={i:count}
        dict_test.update(r1)

    dict_test = sorted(dict_test.items(),key=lambda x:x[1],reverse=True)
    dict_test = Counter(dict_test).most_common(counter_sum)
    return 

def stats_text_cn(text, counter_sum): 
    if not isinstance(text,str): 
        raise ValueError ("please input string type!")
    if not isinstance(counter_sum,int): 
        raise ValueError ("please input int type!")

    text = [chaifen for chaifen in jieba.cut(text)  if len(chaifen) >= 2]# 默认是精确模式

    cn_words = []
    for word in text:        
        if '\u4e00' <= word <= '\u9fff':
            cn_words.append(word)
    counter = {}
    counter_sum = int(counter_sum)

    cn_word_set = set(cn_words)
    for word in cn_word_set:
        counter[word] = cn_words.count(word)
    counter =  sorted(counter.items(), key=lambda x: x[1], reverse=True)
    counter = Counter(counter).most_common(counter_sum)
    return counter


def stats_text(text, counter_sum): #实现功能：分别调⽤用stats_text_en , stats_text_cn ，输出合并词频统计结果
    if not isinstance(text,str): 
        raise ValueError ("please input string type!")     
    if not isinstance(counter_sum,int): 
        raise ValueError ("please input int type!")
    counter_sum = int(counter_sum)

    link_word_1 = stats_text_en(text,counter_sum)
    link_word_2 = stats_text_cn(text,counter_sum)
    link_word = link_word_1 + link_word_2
    return link_word

