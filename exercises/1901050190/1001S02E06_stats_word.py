t = '''
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
优美胜于丑陋
明了胜于晦涩
简洁胜于复杂
复杂胜于凌乱
扁平胜于嵌套
间隔胜于紧凑
可读性很重要
即便假借特里的实用性之名，也不可违背这些规则
不要包含所有错误，除非你确定需要这样做
当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案
虽然这并不容易，因为你不是 Python 之父
做也许好过不做，但不假思索就动手还不如不做
'''
import re    #引入正则表达式，以便操作字符串
import collections   #引入collections模块，以便使用计数功能
def stats_text_en(t):
    t = re.sub("[^A-Za-z]", " ", t)
    t = t.lower()
    t = t.split()
    t = collections.Counter(t)
    print('英文单词词频: \n',t)

def stats_text_cn(t):
    t = re.sub("[A-Za-z.。，,'！\-* \n]", "", t)
    for t1 in t:
        t1 = t.split() 
    t=collections.Counter(t)         
    print('中文汉字字频：\n',t)

stats_text_en(t)
stats_text_cn(t)
