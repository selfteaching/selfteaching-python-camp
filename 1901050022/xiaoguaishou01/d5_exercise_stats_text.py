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
#使用字典（dict）统计字符串样本text中各个英文单词出现的次数
d = {}
for x in text.split( ):
    if not x in d:
        d[x] = 1
    else:
        d[x] = d[x]+1
print(d)
print("按照出现次数从大到小输出所有的单词及出现的次数")
print (sorted(d.items(), key=lambda d: d[1],reverse=True)) 
