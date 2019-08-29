text='''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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
Namespaces are one honking great idea -- let's do more of those!
'''

text1 = text.replace(',',' ').replace('.',' ').replace("'",' ').replace('--',' ').replace('*',' ')
list1 = text1.lower().split()
dict1 = {}  #新建字典
for i in list1:
    count = list1.count(i)
    n = {i:count}
    dict1.update(n)
print(dict1)
dict1 = sorted(dict1.items(), key=lambda x:x[1], reverse=True) 
 # x is the list, in which we are adding x[1] i.e 2nd element of list to the sort function. 
 # sort(mylist, key=lambda x: x[1]) sorts mylist based on the value of key as applied to each element of the list. 
print(dict1)
