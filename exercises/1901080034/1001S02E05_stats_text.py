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
word_dict = {}
text=text.lower()
import re
pttn=r'[^a-z*\s]'
text=re.sub(pttn,"",text)
# print(text)
words = text.split()
# print(words)
for item in words:
    if  item not in word_dict:
        word_dict[item] = 1
    else :
        word_dict[item] += 1

# print(word_dict)
for key in sorted(word_dict.items(),key=lambda item:item[1], reverse=True):
    print (key)
