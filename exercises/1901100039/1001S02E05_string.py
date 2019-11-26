# 字符串的处理练习

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
'''

print (text)

# 将上文中的“better”替换为“worse”
text_worse = text.replace("better","worse")
print (text_worse)

# 将上文中的“ea”剔除
text_noea = text_worse.replace("ea","")
print (text_noea)


# 将上文中的字母进行大小写翻转
text_swap = text_noea.swapcase()
print (text_swap)

# 对上文中的单词进行排序并输出
import re #引入库
s = re.sub(r'[^\w\s]','',text_noea)  #正则表达式进行剔除
text_sort = sorted(s.split())
print (text_sort)