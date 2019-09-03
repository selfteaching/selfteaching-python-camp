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

#better 替换成 worse
m = text.replace('better','worse')
print(m)

#剔除包含ea的单词
import re

n = re.sub(r'\b[\w]*ea[\w]*\b','',m)
print(n)

#字母大小写翻转
i = n.swapcase()
print(i)

#升序排列
import string
j = i.translate(str.maketrans('','',string.punctuation)) #去掉文中的标点及特殊符号
j_list = j.split()
j_list.sort()
print(j_list)