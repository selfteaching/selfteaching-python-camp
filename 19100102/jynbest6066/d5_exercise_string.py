text = ''' The Zen of Python, by Tim Peters
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
There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!
'''

import re
#拆分text字符串
l = re.split(r"(\W+)", text)
#删除包含ea的单词
for i in l:
    if 'ea' in i:
        l.remove(i)


s0 = ''
#将列表l合并为字符串s1
s1 = s0.join(l)
#将s1中全部的‘better’替换为‘worse’
s1 = s1.replace('better','worse')   

#调用str类的swapcase方法，同时实现大写转小写，小写转大写的功能
s1 = s1.swapcase()   

#将所有的单词按首字母从a到z排列
#将字符串s1转换为列表l2
l2 = re.split(r"\W+",s1)
#将l2中的单词按首字母从a到z排列
l2.sort()
#删除l2中为空的列表元素
while '' in l2:
    l2.remove('')

print(l2)