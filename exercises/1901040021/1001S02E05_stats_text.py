text='''The Zen of Python, by Tim Peters
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

#将string text切片，在切片过程中剔除其中的非英文字符剔除，之后将返回值保存在list中
import re
list=re.split(r'\s*[,.*--!\s]\s*',text) 
print(list)

#发现list中有空格，使用.remove剔除list中的空格
while '' in list:
    list.remove('')
print(list)

#统计list中各英文单词的次数，并将各英文单词及其次数作为key：value对保存在dict中
dict={list[i]:list.count(list[i]) for i in range(len(list))}
print(dict)

#使用function sorted对dict.items 中value按照从大到小排序，将返回值保存在a_list中
a_list=sorted(dict.items(),key=lambda item:item[1],reverse=True)
print(a_list)

#直接将a_list中每个元素的item[0]和item[1]作为key:value对保存在a_dict中，并输出
a_dict={i:j for i,j in a_list}
print(a_dict)
