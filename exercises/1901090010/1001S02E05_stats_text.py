
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

"""
2.统计字符串样本中英文单词出现的次数
一个创建³³名为1001S02E05_stats_text.py的文件
使用字典（dict）统计字符串样本text中各个英文单词出现的次数。示例：{'is': 10, 'better': 9, …}
按照出现次数从大到小输出所有的单词及出现的次数
只统计英文单词，不包括非英文字符的其他任何符号，如连接符号，空白字符等
"""
# 1.替换掉所有的符号
word_str = text.replace(',','').replace('.','').replace('!','').replace('*','').replace('--','')
# 2.按照空格将所有的单词分割开
word_list = word_str.split()
# 3.对单词进行去重操作，作为字典的key
word_one = set(word_list)
# 4.构建一个词频字典
dict = {}
for word in word_one:
    dict[word] = word_list.count(word)
# 5.对之前的词频字典按照value值进行排序
d_list = sorted(dict.items(),key=lambda e:e[1],reverse=True)
new_dict = {}
for item in d_list:
    new_dict[item[0]] = item[1]
# 6.输出，检查结果
print(new_dict)

#------------另一种方法实现-----------
word_dict = {}
text=text.lower()
import re
pttn=r'[^a-z*\s]'
text=re.sub(pttn,"",text)
# print(str)
words = text.split()
# print(words)
for item in words:
	if  item not in word_dict:
	    word_dict[item] = 1
	else :
	    word_dict[item] += 1
# print(word_dict)
for key in sorted(word_dict.items(),key=lambda item:item[1], reverse=True):
	    print(key)


