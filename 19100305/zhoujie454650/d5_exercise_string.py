#1.将text中的bettr全部替换为worse
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

a = text.replace('better','worse')
print(a)
#2.大小写字母翻转。
b=a.swapcase()
print(b)
#3.去除带ea的单词
c=b.split()
for d in c:
        if 'EA' in d:
                del d
print(c)
#按照a...z升序排列
c.sort()
print(c)











