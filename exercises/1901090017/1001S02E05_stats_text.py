text ='''
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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
 '''
import re
a = re.sub('[^a-zA-Z \n]','',text)
b = a.split()

#print('正常的英文单词 ==>',b)
counter = {}
#word_set = set(b)
for word in b:
    counter[word] = b.count(word)
print(counter)
c=sorted(counter.items(),key=lambda item:item[1], reverse=True) 
for x in c:
    print(x)