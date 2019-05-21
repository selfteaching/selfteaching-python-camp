str = '''
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
str.replace("better","worse")
new1_str = str.replace("better","worse")
print(new1_str)
import re
pttn=r'[A-Za-z]*ea[A-Za-z]*'
new2_str =re.sub(pttn,"",str)
print(new2_str)
new3_str=new2_str.swapcase()
print(new3_str)
a=new3_str.split()
b=sorted(a)
new4_str=' '.join(b)
print (new4_str)
