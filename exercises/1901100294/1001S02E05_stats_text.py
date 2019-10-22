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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

import collections

list_text = text.split() #讲字符串分割成列表

for a  in range(len(list_text)):
    str_words = list_text[a]    #遍历每一个元素
    b = str_words.strip("*-,.!") #删掉各种出现的特殊字符
    words_new.append(b)

while '' in words_new: #删掉去掉--之后的空元素
    words_new.remove('')

cishu_text = collections.Counter(words_new)  #直接输出统计出现的次数并且按照次数从大到小排列
print(cishu_text)



'''words = text.split()
word_dict = {}
for w in words:
    if w not in word_dict:
        word_dict[w] = 1
    else:
        word_dict[w] = word_dict[w] + 1
print (word_dict)

words_new = []
for a  in range(len(words)):
    str_words = words[a]
    b = str_words.strip("*-,.!")
    print(b)
    words_new.append(b)
print(words_new)'''
