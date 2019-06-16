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
Unless explicitly silenced
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
text=text.replace(',','').replace('!','').replace('--','').replace('.','').replace('*','').lower()
t1=text.split()                                         #变成列表的形式
dicts = {}                                              #创建一个空字典
for i in t1:                                              
    v_number=text.count(i)                              #统计每个单词在text出现的次数，并且复制给v_number
    dicts[i]=v_number                                   #把key和value添加到字典中
print(dicts)
t2= sorted(dicts.items(),key=lambda x:x[1],reverse=True) #对字典按值（value）进行排序
print(t2)
    
