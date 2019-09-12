"""
使⽤用字典(dict)统计字符串串样本text中各个英⽂文单词出现的次数。示例例:{'is':10,
    'better': 9, ...}
3. 按照出现次数从⼤大到⼩小输出所有的单词及出现的次数
4. 只统计英⽂文单词，不不包括⾮非英⽂文字符的其他任何符号，如连接符号、空⽩白字符等
"""

text='''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do 
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! 
''' 

pure_words=text.replace("-"," ")

words = pure_words.split()
d = {}
for word in words:
    d[word] = d.get(word,0) + 1 

print(sorted(d.items(),key=lambda x:x[1],reverse=True))
