# -*- coding: UTF-8 -*-

# Filename : 1001S02E05_string.py
# author by : @shen-huang

# 字符串的基本处理

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

print("1. 字符串的基本处理", end="\n\n")

# ## 将字符串样本 text 里的 better 全部替换成 worse

text2 = text.replace("better", "worse")
# print(text2)

# ## 将字符串 text2 的单词中包含 ea 的单词剔除

# 将 text2 分词，放入 text 3
text3 = re.split(r'(\s|,|\.|—)', text2)
# print(text3)

# 将 text3 中不含 ea 的单词放入 text4
text4 = []
for w in text3:
    if w.find("ea") < 0:
        text4.append(w)

# 把 text4 拼接成 text5，并去掉多余的空格
text5 = "".join(text4)
text5 = re.sub(' {2,}', ' ', text5)
text5 = re.sub('\n ', '\n', text5)
text5 = re.sub(r' \.\n', '.\n', text5)
text5 = re.sub(' —', '—', text5)
text5 = re.sub('— ', '—', text5)
# print(text5)

# ## 将 text5 里的字母进行大小写翻转（将大写字母转成小写，小写字母转成大写）

# text6 = [i.swapcase() for i in text4]
text6 = text5.swapcase()
# print(text6)

# ## 将 text6 里所有单词按a...z升序排列，并输出结果

# 去掉 text6 里的多余符号并添加分词用空格

text7 = re.sub(r',|\.|\*|!', '', text6)
text7 = re.sub('—', ' ', text7)
text7 = re.sub("([0-9A-Za-z]*)'([0-9A-Za-z]*)", "\\1 '\\2", text7)
# print(text7)

# 分词
text8 = re.split(r' |\n', text7)

# 去掉空元素
text8 = [i for i in text8 if i != '']

# 排序
text9 = sorted(text8)

# 拼接成字符串

text10 = " ".join(text9)

# 输出

print(text10)

# print("――――――――――――――――――――――――――――――――――――――――", end="\n\n")
