text='''
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

elements = text.split() #字符串text根据 空白字符（） 分割split成 list，列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。

words = []

symbols = '!-,.*'

for element in elements:
    for symbol in symbols:
        element = element.replace(symbol, '') #判断symbols的元素是否还在单词里，如果在，需要替换成‘’中的元素
    if len(element): # len() 方法返回列表元素个数， if len(element): = if len(element)>0
        words.append(element) # append = 往 words列表 加上 list.append(obj) 

print(words)

counter = {} #dictioan {}

word_set = set(words) # set 可减少words列表里重复的单词，提供 for...in 运算中的效率

for word in word_set:
    counter[word] = words.count(word) #counter字典：包含word_set中的word。count() 方法用于统计字符串里某个字符出现的次数。

print(counter) # counter 字典

print(sorted(counter.items(), key=lambda x: x[1], reverse=True)) # items():a set-like object providing a view on D's items ； key:单词 value：单词出现的次数；x[1] 第一项？？？lambda y: y[1]——>y:y[1]是指字典中统计的数字。？？？key参数传入了一个lambda函数表达式，其x就代表列表里的每一个元素，然后分别利用索引返回元素内的第一个元素。