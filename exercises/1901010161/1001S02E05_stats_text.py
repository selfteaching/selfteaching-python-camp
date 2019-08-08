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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
t = text
t = t.replace(',', '').replace('.', '').replace('!', '').replace('*', '').replace('--', '')
t = t.lower()
t = t.split()
print(t)
t1 = {}
for i in t:
    count = t.count(i)
    a = {i: count}
    t1.update(a)
print(t1)
# 打印一个空行
print('\n')
# reverse，翻转默认排序，从大到小排列
t1 = sorted(t1.items(), key=lambda x: x[1], reverse=True)
print(t1)
