#text文本文件
text ='''
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
#1.将text中的better替换成worse
text1 = text.replace("better","worse")
print(text1)

#2.将text1中包含ea的单词剔除
###转换为列表
list1 = text1.split()
list2 = []
###遍历列表并去除'ea'
for i in list1:
    if 'ea' not in i: 
        list2.append(i)
        print(list2)

#3.list2大小写字母转换
text2 = " ".join(list2)
text3 = text2.swapcase()
print(text3)

#将text3结果里所有单词按a...z排序，并输出结果
list3=[]
for i in list2:
        if i.isupper():
                list3.append(i.lower())
        elif i.islower():
                list3.append(i.upper())
list3.sort()
print(list3)


