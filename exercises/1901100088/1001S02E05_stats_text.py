text='''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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

print("使用字典（dict）统计字符串样本text中各个英文单词出现次数")
test_1 = text.split()
test_2 = []
for word in test_1:
    test_2.append(test_1.count(word))
test_3 = dict(zip(test_1,test_2))
print(test_3)

print("按出现次数从大到小输出所有单词及出现次数")
sort_test = sorted(test_3.items(),key=lambda item:item[1], reverse = True)
print(sort_test)

print("只统计英文单词，不包括非英文单词的其他任何符号，如链接符号、空白字符等")
stat_0 = text.lower()
stats = stat_0.split()
word_1 = []
puns= ',.*-!9'
for stat in stats:
    for pun in puns:
        if pun in stat:
            stat = stat.replace(pun,"")
    if len(stat):
            word_1.append(stat)
print(word_1)
count_word = []
for cw in word_1:
    count_word.append(word_1.count(cw))
stat_2 = dict(zip(word_1,count_word))
print(stat_2)
print()
sort_s2 = sorted(stat_2.items(),key=lambda item:item[1], reverse=True)
print(sort_s2)