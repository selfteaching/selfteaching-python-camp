sample_text = '''
The Zen of Python , by Tim Peters

Beautiful is better than ugly.
Explicit is better than implcit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases are't special enough to break the rules.
Although practicality beats purity.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one --- and preferably only one -- obvious way to do it.
Although the way may not be obvious at first unless you are a Dutch.
Now is better than never.
Although never is better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it's maybe a good idea.
Namespaces are one honking great idea --- let's do more of those!
'''

#1. 使用字典统计样本中英文单词出现次数

elements = sample_text.split()
words = []
symbols = ', . * - !'
for element in elements:
    for symbol in symbols:
        element = element.replace(symbol, '')
    if len(element) != 0:
        words.append(element)
print('正常的英文单词 ==>', words) 

#单词出现次数
counter = {}
word_set = set(words)

for word in word_set:
    counter[word] = words.count(word)
print('单词出现次数 ==>', counter)

#出现次数从大到小排序

print('从大到小输出所有单词出现的次数 ==>', sorted(counter.items(), key=lambda x: x[1], reverse=True))