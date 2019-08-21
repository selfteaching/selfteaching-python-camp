from collections import Counter 

#统计参数中每个英⽂单词出现的次数
def stats_text_en(text, count):          
    elements = text.split()           
    words = []                        
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol, '')             
        if len(element) and element.isascii():   
            words.append(element)                             
    return Counter(words).most_common(count) 

#统计参数中每个中⽂单词出现的次数
def stats_text_cn(text, count):           
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':    
            cn_characters.append(character)
    return Counter(cn_characters).most_common(count) 
    

def stats_text(text, count):  
    if not isinstance(text, str):
        raise ValueError('参数必须是 str 类型，输入类型 %s' % type(text))      
    return stats_text_cn(text, count) + stats_text_en(text, count) 

en_text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly 88.
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


cn_text = '''
简洁胜于复杂
复杂胜于凌乱
扁平胜于嵌套
间隔胜于紧凑
可读性很重要
即便假借特例的实用性之名，也不可违背这些规则
当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案
虽然这并不容易，因为你不是 Python 之父
做也许好过不做，但不假思索就动手还不如不做
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然
命名空间是一种绝妙的理念，我们应当多加利用
'''
