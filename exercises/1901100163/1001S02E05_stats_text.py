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

dict1 = {}

import re
list1 = re.split(r"\W+",text)   #将字符串text转换为列表list1,只保留单词为list1中的元素
while '' in list1:   #删除list1中为空的列表元素
    list1.remove('')
    
for i in list1:   #i属于list1中的元素，开始循环
    dict1.setdefault(i,list1.count(i))   #将列表中的单词及单词的出现次数，分别赋值给dict1的键和值
    
tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)   #将dict1按照value值从大到小排列，并将结果赋给元组tup1
dict2 = {}

for tup1 in tup1:   #遍历元组tup1
        dict2[tup1[0]] = dict1[tup1[0]]   

print("最终结果为:")  
print(dict2)



