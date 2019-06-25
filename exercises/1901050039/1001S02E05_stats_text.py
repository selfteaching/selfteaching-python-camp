#使用词典统计单词出现次数
#从大到小排序

#输入文本
 
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

#使用词典统计次数
t1 = text.split() # 先转换为list
from collections import Counter #引入counter模块
res = Counter(t1)

#排序
d = dict(res) #转换为词典
d2 = sorted(d.items(),key=lambda a: a[1],reverse=True) #用sort排序
d2 = dict(d2) #转换为词典
print(d2)

