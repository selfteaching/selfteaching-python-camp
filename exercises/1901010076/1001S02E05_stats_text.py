#作者：邓超
#编号：1901010076
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
text_list1 = text.split()   #形成单词列表
text_list2 = []               #列表用方括号括起来
for d in text_list1:            #遍历text_list1中的每个单词
    if d.isalpha():               #如果d中的所有字符都是字母则返回True
        text_list2.append(d)        #去除非单词
dict1 = {}                                      #让dict2等于{}
dict1 = dict(dict1)                               #转化为字典
print(dict1) 



 












text_list1 = text.split()   #形成单词列表
text_list2 = []               #列表用方括号括起来
for d in text_list1:            #遍历text_list1中的每个单词
    if d.isalpha():               #如果d中的所有字符都是字母则返回True
        text_list2.append(d)        #去除非单词
dict1 = {}                            #标准的映射类型字典。字典的键几乎是任意值
dict1 = dict1.fromkeys(text_list2)      #对dict1改变成键值来自于text_list2
word_1 = list(dict1.keys())               #赋值word_1是表dict1的键值
for d in word_1:                            #遍历word_1的值，并储存到i
    dict1[d] = text_list2.count(d)            #统计单词出现的次数，
dict2 = {}                                      #让dict2等于{}
dict2 = sorted(dict1.items(), key=lambda d : d[1], reverse=True)#按values进行排序，
dict2 = dict(dict2)                               #转化为字典
print(dict2)

