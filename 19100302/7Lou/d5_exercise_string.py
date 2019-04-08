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
text=text.replace('better','worse')
text=text.split()#转换为列表

l=[]
for i in text:#遍历列表
        if 'ea' not in i: 
                l.append(i)#去除'ea'的列表
text=" ".join(l)#将列表转换为字符串
text=text.swapcase()#翻转大小写字母
text=text.split()#转换为列表
#print(sorted(text)) sort只用于列表；sorted可用于所有可迭代对象。
text.sort()
print(text)

