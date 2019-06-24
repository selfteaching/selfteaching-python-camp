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
In the face of ambxiquity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
#better全部替换成worse
i=text
r=i.replace('better','worse').replace('*',' ').replace('!',' ').replace('--',' ').replace(',',' ')
print(r)
#剔除包含ea的单词
s=r.split()
t='ea'
u=[]
for p in s:
    if p.find(t)<0:
        u.append(p)
print(u)
#大小写翻转
print(" ".join(u))
u=" ".join(u)
z=u.swapcase()
print(z)
#按a-z升序排序
print(z.split())
z=z.split()
z.sort()
print(z)