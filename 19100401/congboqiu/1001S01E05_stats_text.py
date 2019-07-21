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
dictionary={}#创建字典

text=text.replace(',',' ').replace('.',' ').replace('*',' ').replace('--',' ')
text1=text.split()
print(text1)

for i in text1:
    dictionary.update({i:text1.count(i)})#通过key:计数函数来更新字典
print(dictionary)

dictionary1=sorted(dictionary.items(),key=lambda x:x[1],reverse=True)#sorted()排序;.items()遍历字典(键,值) 元组,
print(dictionary1)                                  #key=lambda x:x[1],按元组第右边的值1排升序，reverse=True反转