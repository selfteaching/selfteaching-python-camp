text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
unless explicitly silenced.
In the face of ambxiguety, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- lets's do more of those!
'''

# 对text进行拆分
text_list = text.split()
# 对拆分的列表进行整理，剔除其它字符
text_list = [x.strip(',.-!*').replace('\'','') for x in text_list if x.strip(',.-!*') != ''] 

# 将整理好的列表按顺序加入字典，如果key不再字典中，则加入字典并将对应value赋值为1；如果key在字典中，则对应value值+1
words_dict = {}
for word in text_list:
    if word in words_dict.keys():
        words_dict[word] = words_dict[word] + 1
    else:
        words_dict.update({word:1})

# 对得到的字典按value值进行排序
statistic = sorted(words_dict.items(), key=lambda x:x[1], reverse = True)
print(statistic)






