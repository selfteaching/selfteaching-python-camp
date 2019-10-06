# a-better换成worse，b-剔除含ea的单词，c-翻转大小写，d-单词按a-z排列并输出

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

import re

a = text.replace('better', 'worse')
# print(a)

# import re
findb = re.compile(r'(\w*ea\w*)') #先写对象效率高
b = findb.sub('', a)
# print(b)

c = b.swapcase()
# print(c)

cut = re.compile(r'[-.*,!]')
cutc = cut.sub('',c)
# print(cutc)
d1 = sorted(cutc.split(), key=str.lower)
st = '\t'
d = st.join(d1)
print(d)