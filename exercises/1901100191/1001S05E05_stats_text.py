s='''
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
Namespaces are one honking great idea -- let's do more of those!'''
i=s.split()
b=[]
d=',.*!-'
for e in i:
    for f in d:
        e=e.replace(f,'')
    if len(e):
        b.append(e)
print(b)
g={}
b_set=set(b)
for h in b_set:
    g[h]=b.count(h)
print(g)
print(sorted(g.items(),key=lambda x: x[1],reverse=True))