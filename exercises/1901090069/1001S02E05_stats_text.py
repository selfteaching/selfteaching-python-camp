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

#将文本中的非英文单词符号用空格替换
text = text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
#将文本统一为小写字母，方便统计
text = text.lower()
#以默认（所有的空字符，包括空格、换行(\n)、制表符(\t)等）为分隔符对字符串进行切片，从而达到提取所有英文单词的效果
text = text.split()
#创建字典，遍历text，统计各单词出现次数，并以单词及对应出现次数为键值对存入字典
dict1 = {}
for i in text:
    count = text.count(i)
    dict2 = {i:count}
    dict1.update(dict2)
print(dict1)
#用内置函数sorted（）实现按照单词出现次数，从大到小排序
dict1 = sorted(dict1.items(),key=lambda x:x[1],reverse=True) 
print(dict1)