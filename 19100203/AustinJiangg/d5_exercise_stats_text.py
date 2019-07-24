text = ''' The Zen of Python, by Tim Peters
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those! '''

textlist1 = text.split()#形成单词列表
textlist2 = []
for i in textlist1:
    if i.isalpha():
        textlist2.append(i)#去除非单词

dict1 = {}
dict1 = dict1.fromkeys(textlist2)#将textlist2的元素作为dict1的键值key
word_1 = list(dict1.keys())
for i in word_1:
    dict1[i] = textlist2.count(i)#统计单词出现的次数
dict2 = {}
dict2 = sorted(dict1.items(),key=lambda d:d[1],reverse=True)#按values进行排序
dict2 = dict(dict2)#转化为字典
print(dict2)
