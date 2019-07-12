#-*- coding: UTF-8 -*- 
import collections
import os
import jieba
import chardet

#text = 
'''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#text_cn = 
'''

来自管理员童鞋的回复：可以自己定义哈，主要是实现函数的功能
完成时可以自己写一些测试的参数，检验自己的函数功能是否正确

'''

def stats_text_en (text): #sort English words by the frequency.
    try:
        for i in range(len(text)):
            if (text[i] >= u'\u0041' and text[i]<=u'\u005a') or (text[i] >= u'\u0061' and text[i]<=u'\u007a'):
                break


        text_en = text[i:]
        text_en = text_en.replace('--', '')
        text_en = text_en.replace('!', '')
        text_en = text_en.replace('*', '')
        text_en = text_en.replace('.', ' ')
        text_en = text_en.replace(',', '')

        # print("CN words frequency: ")
        # print(text_en)

        text_en = text_en.split()

        counter_en = collections.Counter(text_en)
        print("\n\nEN words frequency: ")
        print(counter_en)

        return counter_en

    except TypeError:
        print("English sorting: TypeError catched!")
        

def stats_text_cn (text, max_counts): #sort Chinese words by the frequency. Only output the first 100!
    try:
        text_cn = ''

        for ch in text:
            if u'\u4e00' <= ch <= u'\u9fff': #only fetch the Chinese characthers
                text_cn = text_cn + ch
        #text_cn = text_cn.encode("utf-8")
        
        text_jieba = " ".join(jieba.cut(text_cn, cut_all=True))

        text_jieba_split = text_jieba.split()
       

# ''' previous homework without jieba:
#         text_split = []

#         for i in range(len(text_cn)):
#             text_split.append(text_cn[i])
#'''

    
        counter_cn = collections.Counter(text_jieba_split)
        counter_cn = collections.Counter(counter_cn).most_common(max_counts)


        print("The most common " + str(max_counts)+ " CN wrods: ")
        print(counter_cn)
        return dict(counter_cn)

    
    except TypeError:
        print("Chinese sorting: TypeError catched!")



def stats_text (text): #call the functions above

    try:        
        stats_text_cn (text, 20)
        stats_text_en (text)
    except TypeError:
        print("Text sorting: TypeError catched!")
    

