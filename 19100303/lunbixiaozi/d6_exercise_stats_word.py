#-*- coding: UTF-8 -*- 
import collections
import os

text = '''
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

text_cn = '''

来自管理员童鞋的回复：可以自己定义哈，主要是实现函数的功能
完成时可以自己写一些测试的参数，检验自己的函数功能是否正确

'''

def stats_text_en (text): #sort English words by the frequency.
    
    text = text.replace('--', '')
    text = text.replace('!', '')
    text = text.replace('*', '')
    text = text.split()

    return collections.Counter(text)




def stats_text_cn (text): #sort Chinese words by the frequency.

    text = text.replace('：', '')
    text = text.replace('，', '')
    text = text.replace('\n', '')
    #text = text.replace('*', '')
    print ('first char:')
    print (text[0])

    text_split = []

    for i in range(len(text)):
        text_split.append(text[i])

    #text = text.split()

    return collections.Counter(text)

print(stats_text_cn(text_cn))




