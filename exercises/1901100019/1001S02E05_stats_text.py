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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

# 去掉所有的标点符号
text1 = text.replace('.', ' ')
text2 = text1.replace(',', ' ')
text3 = text2.replace('--', ' ')
text4 = text3.replace('!', ' ')
text5 = text4.replace('*', ' ')

# 转换成列表
list1 = text5.split()

# 从列表中统计每个单词的个数，并写入字典
dict1 = {}
while len(list1) > 0:
    if list1[0] in dict1.keys():
        dict1[list1[0]] += 1
    else:
        dict1[list1[0]] = 1
    del list1[0]


# 将字典按单词的个数排序
list2 = sorted(dict1.items(), key=lambda x:x[1], reverse=True)
print(list2)