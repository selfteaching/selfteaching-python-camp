t = '''
2 The Zen of Python, by Tim Peters
345 Beautiful is better than ugly.
6 Explicit is better than implicit.
7 Simple is better than complex.
8 Complex is better than complicated.
9 Flat is better than nested.
10 Sparse is better than dense.
11 Readability counts.
12 Special cases aren't special enough to break the rules.
13 Although practicality beats purity.
14 Errors should never pass silently.
15 Unless explicitly silenced.
16 In the face of ambxiguity, refuse the temptation to guess.
17 There should be one-- and preferably only one --obvious way to do
it.
18 Although that way may not be obvious at first unless you're Dutch.
19 Now is better than never.
20 Although never is often better than *right* now.
21 If the implementation is hard to explain, it's a bad idea.
22 If the implementation is easy to explain, it may be a good idea.
23 Namespaces are one honking great idea -- let's do more of those!
'''
t = t.replace(',',' ').replace('.',' ').replace('--',' ').replace('*',' ').replace('!',' ')
t = t.lower() #所有英文字符转换成小写，不然the和The会分别统计
t = t.split() #拆分成字符串，才能以单词为单位进行统计，拆分后变为列表
t1 = {} #建立一个空字典
for i in t:
    count = t.count(i)
    d = {i:count}
    t1.update(d)
print(t1)
print('\n')
t1 = sorted(t1.items(),key = lambda x:x[1],reverse = True)
print(t1)