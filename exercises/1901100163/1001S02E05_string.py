#原始文本
text='''
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
Namespaces are one honking great idea -- let's do more of those!'''
str1=text.replace('better','worse')
print(str1)
list1=str1.split() #转换为列表
print(list1)
list2=[]
for i in list1:
    if 'ea' not in list1:
        list2.append(i) #去除ea的列表
print(list2)
tup1=(' '.join(list2))
tup2=tup1.swapcase()
#print(tup2)
print(sorted(tup2.split(), key=str.lower))