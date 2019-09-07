# -*- coding: UTF-8 -*-

# Filename : 1001S02E05_string.py
# author by : @shen-huang

# 词频统计

import re  # 正则表达式

text = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren’t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one—and preferably only one—obvious way to do it.
Although that way may not be obvious at first unless you’re Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it’s a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea—let’s do more of those!"""

print("2. 统计字符串样本中英文单词出现的次数", end="\n\n")

# 去掉 text 里的多余符号和空格，添加分词用空格，全文转为小写

text2 = re.sub(',|\\.|\\*|!', '', text)
text2 = re.sub('—', ' ', text2)
text2 = re.sub("([0-9A-Za-z]*)'([0-9A-Za-z]*)", "\\1 '\\2", text2)
text2 = re.sub("\n", " ", text2)
text2 = re.sub(" +", " ", text2)
text2 = str.lower(text2)
# print(text2)

# 分词，去掉空元素，排序
text3 = re.split(" ", text2)
text3 = [i for i in text3 if i != '']
text3 = sorted(text3)
# print(text3)

# 生成非重复单词列表
text4 = []
[text4.append(w) for w in text3 if w not in text4]
# # 列表推导式等价写法——
# for w in text3:
#     if not w in text4:
#         text4.append(w)
# print(text4)

# 生成词频统计字典
text_freq = {w: text3.count(w) for w in text4}
# text_freq_tuple = text_freq.items()  # 把字典转换成一个由元组构成的列表
# print(text_freq_tuple)

# 按词频排序
text_freq = sorted(text_freq.items(), key=lambda freq: freq[1], reverse=True)
# text_freq_tuple.sort()  # 不能用 sort()，只能用 sorted()
text_freq = dict(text_freq)

# 输出
print(text_freq)

# print("――――――――――――――――――――――――――――――――――――――――", end="\n\n")
