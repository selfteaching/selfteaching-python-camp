

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
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

#首先，分割文本为单词，但会有标点符号，后面还需要处理掉
words01 = text.split()

#定义一个空列表，用于存储处理后的单词们
words02 = []

#定义需要删除的标点
symbols = ',.-*'
#用空字符替换的方法删除标点符号
for word01 in words01:
    for symbol in symbols:
        word01 = word01.replace(symbol,'')
    if len(word01):
        words02.append(word01)

print('处理后的英文单词列表', words02)


#初始化一个字典
counter = {}
words_set = set(words02)
#统计单词出现次数
for word in words_set:
    counter[word] = words02.count(word) #完成键值的匹配，即生成了字典的元素们
print('以字典形式输出单词重复次数', counter)

#使用sorted，依据key的降序排列字典
print('降序排列字典', sorted(counter.items(), key = lambda x : x[1], reverse=True))

print('以键，升序排列字典', sorted(counter.items(), key = lambda x : x[0]))

