text='''
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#把text里的better替换成worse
t1 = text.replace('better','worse')

#将单词中包含ea的单词剔除
t2 = t1.split()
str1 = 'ea'
str2 = []
for x in t2:
    if x.find(str1) == -1:
        str2.append(x)
str3 = ' '.join(str2)

#将字母进行大小写翻转
t3 = str3.swapcase()

#单词按a-z升序排列
t4 = t3.replace('9','')
import re
pattern = re.compile(r'\w+')
t5 = pattern.findall(t4)
print(sorted(t5,key=lambda T: (T.lower(),T)))
