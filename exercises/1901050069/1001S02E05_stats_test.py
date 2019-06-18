simple_text = '''
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

# 1. 使⽤字典（dict）统计字符串样本 text 中各个英⽂单词出现的次数

#先将字符串根据空白字符分割成 list，要调用 str 类型
elements = simple_text.split()

# 定义一个新的 list 型变量，存储处理过的单词
words = []

# 挑出需要剔除的非单词符号
symbols = ',-*_!'

for element in elements:
    for symbol in symbols:
        element = element.replace(symbol,'')
        if len(element):
            words.append(element)
print(words)

counter = {}
word_set = set(words)
for word in word_set:
    counter[word] = words.count(word)
print(counter)

# 2.按照出现次数从⼤到⼩输出所有的单词及出现的次数
print(sorted(counter.items(),key = lambda x: x[1]))
