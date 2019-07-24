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

# 2、使用字典统计字符串样本text中各个英文单词出现的次数。实例：{'is':10, "better":9, ...}
word_list = text.replace("--",'').replace("*",'').replace('\n', ' ').split(" ")
dict = {}
for word in word_list[:]:
    if word == '':
        word_list.remove(word)
    elif word not in dict:
        dict[word] = 1
    else:
        dict[word] = dict.get(word) + 1
print(dict)



# 3、按照出现次数从大到小输出所有的单词及出现的次数
print(sorted(dict.items(),key=lambda x:x[1],reverse=True))



# 4、只统计英文单词，不包括非英文字符的其他任何符号，如连接符号、空白字符等
word_list = text.replace("--",'').replace("*",'').replace('\n', ' ').split(" ")
for word in word_list[:]:
    if word == '':
        word_list.remove(word)
print("总共 %d 个英文单词。" % len(word_list))













