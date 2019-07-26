def stats_text_en(text):
    """输入一个英文字符串，统计字符串种每个英文但此出现的次数，最后返回一个按词频降序排列的数组。
    """
    
    # 将输入的字符串分词并整理成小写单词的列表
    text_list = text.split()
    text_list = [x.strip('!,.-!*').replace('\'','').lower() for x in text_list if x.strip('!,.-!*') != '']
    
    # 根据将整理好的列表统计每个单词出现的次数，用字典存储
    word_dict = {}
    for word in text_list:
        if word in word_dict.keys():
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict.update({word:1})
    
    # 返回降序排列的单词列表
    words = sorted(word_dict.items(), key=lambda x:x[1], reverse = True)
    return [x[0] for x in words]


def stats_text_cn(text):
    """
    统计参数中每个中文汉字出现的次数，返回一个按字频降序排列的数组
    """
    
    # 将字符串变成一个单个中文字组成的列表
    text_list = [word for word in text if '\u4e00' <= word <= '\u9fff']
    
    # 生成记录每个中文字出现次数的字典
    counter = {}
    cn_set = set(text_list)
    for word in cn_set:
        counter[word] = text_list.count(word)
    
    words = sorted(counter.items(), key=lambda x:x[1], reverse = True)
    return [x[0] for x in words]
    


text_en = '''
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

text_cn = '''
统计参数中每个中文汉字出现的次数，返回一个按字频降序排列的数组
'''

print(stats_text_en(text_en))
print()
print(stats_text_cn(text_cn))
