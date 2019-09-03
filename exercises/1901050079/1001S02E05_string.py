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
# better 变成 worse
a=text.replace('better','worse')
# 去掉 包含 ea 的单词
b=a.split()
c=[]
for x in b:
    if x.find('ea')<0:
        c.append(x)
# 大小写转换
d=' '.join(c)
e=d.swapcase()
# 字母排序
f=e.replace('*',' ').replace('--',' ')
g=f.split()
h=sorted(g)
print(h)