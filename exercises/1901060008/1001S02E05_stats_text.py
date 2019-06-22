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
print('第一题：统计字符串text中各个单词出现的次数\n')
t=text.replace(',','').replace('.','').replace('--','').replace('*','')   #首先把多余的标点符号去掉。
t1=t.split()
dict_str={}
for key in t1:
        count=t1.count(key)
        dict_str[key]=count
print(dict_str)
print('*'*50)
print('第二题：按照次数大小进行排序\n')
t2=sorted(dict_str.items(),key=lambda items:items[1],reverse=True)   #这个句式还不是很明白，后续需要抽时间好好研究
print(t2)
