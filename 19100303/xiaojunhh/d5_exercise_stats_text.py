
# 原始文本
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


# 只统计英文单词，不包括非英文字符的其他任何符号，如连接符号、空白字符等等
list1 = text.split( )
i=0
for i in range(0,len(list1)):
    list1[i]=list1[i].strip('*-,.!')
    if list1[i]==' ': 
        list1[i].remove(' ')
    else:
        i=i+1
# 使用dict统计字符串样本中各个英文单词出现的次数
# 按照出现次数从大到小排列，示例 {'is': 10, ‘better’ : 9, …… }
import collections
print(collections.Counter(list1))


dict={}
for i in text:
    count=list1.count(i)
    r1={i:count}
    dict.updat(r1)
print(dict)

dict1=sorted(dict.items(),key=lambda x:x[1],reverse=True)
print(dict1)