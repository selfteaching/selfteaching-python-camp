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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#使⽤字典（ dict）统计字符串样本 text 中各个英⽂单词出现的次数

#单词列表
word_list = re.sub(r'[\-\*\.\-!,]', '', text.lower()).split()  #单词小写，去除标点，只留单词,并将字符串分拆成单词列表

word_dict = {}

word_dict = {word:word_list.count(word) for word in word_list}

result = sorted(word_dict.items(), key = lambda item: item[1], reverse = True)

print(result)