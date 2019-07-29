'''
stats_text
time：2019年7月18日22:00:42
version:1.0
'''
text ='''
The Zen of Python, by Tim Peters


Beautiful is better than guly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although particality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one -- and preferably only one -- obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it's may be a good idea.
Namespace are one honking great idea -- let's do more of those!
'''

#1.使用字典（dict)统计各单词出现的次数
#第一步：清洗非单词元素
elements = text.split()
words =[]
symbols = ',.!*-'
for element in elements:
    for symbol in symbols:
        element = element.replace(symbol,'')
    if len(element):
        words.append(element)
print('清洗完成后的纯单词==>',words)

#第二步：列出dict的两个重要参数：keys,kwgs
counter={}
word_set = set(words)
#for word in words:
for word in word_set:
    counter[word]=words.count(word)
print(counter)
#回顾：单词的清洗是基础，排除不必要的干扰，然后分别列出dict的两个参数。

#2、按照出现次数从大到小输出所有单词及次数
#思路：利用sorted函数，出现次数作为参数
print(sorted(counter.items(),key = lambda x:x[1], reverse = True))
#reverse = true表示按照降序排列