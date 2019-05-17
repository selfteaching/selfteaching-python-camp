# Filename : 1001S02E06_stats_word.py
# author by : 张金磊

from collections import Counter
import re

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
曾经沧海难为水，除却巫山不是云。溪云初起日沉阁,山雨欲来风满楼
'''

#定义函数用于去除英文文本中的其他字符（!"#$%&()*+,-./;:<=>?@[\\]^‘_{|}~）和中文
def getText(text):
    txt = text
    txt = txt.lower()
    result = re.sub("[^A-Za-z]", " ", txt.strip())
    for ch in '!"#$%&()*+,-./;:<=>?@[\\]^‘_{|}~':
        result = result.replace(ch, " ")
    return result

#定义函数用于统计英文单词词频，并按词频降序输出 
def stats_text_en(text):
    hamletTxt = getText(text)
    words = hamletTxt.split()
    word = Counter(words)
   
    print('英文单词词频统计结果：','\n', word)    
    

#定义函数用于统计中文汉字字频，并按字频降序输出
def stats_text_cn(text):
    result = re.findall(u'[\u4e00-\u9fff]+', text)    #汉字的unicode范围
    words = ''.join(result)
    word = Counter(words)
   
    print('汉字词频统计结果：','\n', word)   
    
####教练代码借鉴
#import collections
#import re

#def stats_text_en(text):
    
    #result = re.sub("[^A-Za-z]", " ", text.strip())
    #newList = result.split()
    #print('英文单词词频统计结果： ',collections.Counter(newList),'\n')

#def stats_text_cn(text):
    #result1 = re.findall(u'[\u4e00-\u9fff]+', text)
    #newString = ''.join(result1)
    #print('汉字词频统计结果： ', collections.Counter(newString), '\n')
    
#stats_text_en(text)
#stats_text_cn(text)