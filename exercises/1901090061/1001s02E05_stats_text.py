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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
#将长字符串中的非英文单词用空格替换
text = text.replace(',','').replace('.','').replace('!','').replace('-','').replace('*','')
text = text.lower()#全部切换为小写
text = text.split()#提取单词
dict_1 = {}#创建字典
for i in text:#单词遍历
    num = text.count(i)#统计单词出现次数
    dict_2 = {i : num}#将单词，频次数据录入字典
    dict_1.update(dict_2)#更新字典，不更的话只显示一个单词……
dict_1 = sorted(dict_1.items(),key = lambda x:x[1], reverse = True)
print(dict_1)