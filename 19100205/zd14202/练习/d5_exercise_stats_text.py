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
text = text.replace(',', ' ').replace('.', ' ').replace( '--', ' ').replace('!', ' ').replace('*', ' ') #要求只统计英文单词的频次，不包括其他任何符号，所以这一步是删除无关符号，只剩单词。
text = text.split() #split()就是将一个字符串分裂成多个字符串组成的列表。
text1={} #创建字典数据类型。
for i in text: #for循环。对在text中的每一个单词执行如下操作：
    quantity=text.count(i) #计数text中单词的数量
    text2={i:quantity} #创建字典数据类型。键为单词，值为频率计数值。
    text1.update(text2) #字典 update() 函数把字典参数 text2 的 key/value(键/值) 对更新到字典 text1 里。
print(text1) #打印text1
text3=sorted(text1.items(),key=lambda x:x[1],reverse=True)
print(text3) 