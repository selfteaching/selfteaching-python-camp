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

#1.将better替换为worse
s = text.replace('better','worse')
print(s)

#2.剔除含有ea的单词
a="EA"
b=[]
for a in s:
    if a.find(s)<0:
        b.append(a)
print(s)

#3.大小写替换
y=s.swapcase()
print(y)

#4.升序排列
list1=y.split()
list1.sort()
print(list1)