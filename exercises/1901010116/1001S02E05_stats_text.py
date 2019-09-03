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

import string
m = text.translate(str.maketrans('','',string.punctuation)) #去除标点及其余的符号

#拆分字符串
m_list = m.split()

m_dict = {}  #定义一个空字典
m_dict = m_dict.fromkeys(m_list) #去掉重复单词

#统计单词出现次数
for i in m_dict.keys():
    m_dict[i] = m_list.count(i)

#按照出现次数从大到小输出所有单词及次数
for key,value in sorted(m_dict.items(),key = lambda d:d[1],reverse = True):
    print(key,value)