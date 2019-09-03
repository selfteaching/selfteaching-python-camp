a='''
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
# text=a.replace('better','worse')
# print(text)
# 神一般看不太懂的正则表达式，不过有意思，明明没有x.replace('被替换','替换为')方法易于理解，但是这种表达一定有什么优势？
import re
strinfo=re.compile('better')
b=strinfo.sub('worse',a)
print(b)

c=b.split() # 对于电脑来说，一个文本里有大量字符和各类符号组成，先将文档中每个单词转入列表
d=[]
[d.append(e) for e in c if e.find('ea')<0]
print(d)
# f=' '.join(d)# 把列表转换为字符串
# print(f)

g=[h.swapcase() for h in d]
print(g)
print(sorted(g))
# print(sorted(g),reverse=Ture) 降序排列
