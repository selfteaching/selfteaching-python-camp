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

# 使用字典dict 统计字符串样本text 中各个英文单词出现的次数。
print('统计英文单词出现的次数\n')
t1 = text.split()
t2 = []
for x in t1:
    if x.isalpha():
        t2.append(x)
dict1 = {}
dict1 = dict1.fromkeys(t2)
word_1 = list(dict1.keys())
for x in word_1:
    dict1[x] = t2.count(x)
print(dict1)

print('\n按照出现次数大小输出所有单词\n')
dict2 = {}
dict2 = sorted(dict1.items(), key=lambda d : d[1], reverse=True)
dict2 = dict(dict2)
print(dict2)