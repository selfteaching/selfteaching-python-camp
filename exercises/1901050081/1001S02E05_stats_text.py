 
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
text1=text.lower()
import re
pattern=re.compile(r'\w+')
result=pattern.findall(text1)
list1=list(result)
set1=set(list1)
list2=list(set1)
print('\n')
d1={}
for a in range(len(list2)):
    d1[list2[a]]=0
    for b in range(len(list1)):
        if list2[a]==list1[b]:
            d1[list2[a]]+=1
print(sorted(d1.items(), key=lambda x:x[1], reverse=True))