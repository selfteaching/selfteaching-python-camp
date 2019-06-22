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

# better替换成wose
t1 = text.replace('better','worse')
print(t1)

# 剔除包含ea的单词
t2 = t1.split()
t3 = []
for i in t2:
    if 'ea' not in i:
        t3.append(i)
print(t3)

# 大小写翻转
t4 = ''.join(t3)
T4 = t4.swapcase()
print(T4)

#将所有单词按照a...z升序排列

t3.sort()
print(t3)