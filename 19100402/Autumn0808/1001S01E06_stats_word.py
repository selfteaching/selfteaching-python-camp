#text文本文件
text ='''
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
红酥手，黄藤酒，满城春色宫墙柳。等闲识得东风面，万紫千红总是春。
'''
###定义函数用于统计英文单词词频，并按词频降序输出
def stats_text_en(text):
    counten={}
    for x in text:
        if x in text:
           counten[x]=text.count(x)
        else:
           counten[x]=text.count(x)+1
    return counten
print(sorted(stats_text_en(text.split()).items(),key=lambda item:item[1],reverse=True))

###定义函数用于统计中文汉字字频，并按字频降序输出
def stats_text_cn(text):   
    countcn={}
    for i in text:
        if u'\u4e00'<=i<=u'\u9fff':
            countcn[i]=text.count(i)
        else:
            countcn[i]=text.count(i)+1
    return countcn
print(sorted(stats_text_cn(text).items(),key=lambda item:item[1],reverse=True)) 

###教练代码借鉴
import collections
import re

def stats_text_en(text):
    
    result = re.sub("[^A-Za-z]", " ", text.strip())
    newList = result.split()
    print('英文单词词频统计结果： ',collections.Counter(newList),'\n')

def stats_text_cn(text):
    result1 = re.findall(u'[\u4e00-\u9fff]+', text)
    newString = ''.join(result1)
    print('汉字词频统计结果： ', collections.Counter(newString), '\n')
    
stats_text_en(text)
stats_text_cn(text)