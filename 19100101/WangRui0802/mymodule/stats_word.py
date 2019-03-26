# 一个中英混杂的文本
str = '''
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
Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。
'''

import collections
import re
    
def stats_text_en(en,count):
    ''' 1. 英文词频统计。
        2. 参数类型检查，不为字符串抛出异常。
    '''
    if type(en) == str: 
            text_en = re.sub("[^A-Za-z]", " ", en.strip())
            enList = text_en.split( )
            return collections.Counter(enList).most_common(count)
    else:
        
            raise ValueError('type of argumengt is not str')
    
def stats_text_cn(cn,count):
    ''' 1. 汉字字频统计 
        2. 参数类型检查，不为字符串抛出异常。
    '''
    if type(cn) == str : 
            cnList = re.findall(u'[\u4e00-\u9fff]+', cn.strip())
            cnString = ''.join(cnList)
            return collections.Counter(cnString).most_common(count)
    else:
        
            raise ValueError ('type of argumengt is not str')
    
def stats_text(text_en_cn,count_en_cn) :
    ''' 1. 合并英汉词频统计 
        2. 参数类型检查，不为字符串抛出异常。
    '''
    if type(text_en_cn) == str: 
            return (stats_text_en(text_en_cn,count_en_cn)+stats_text_cn(text_en_cn,count_en_cn))
    else:
        
            raise ValueError ('type of argumengt is not str')
    