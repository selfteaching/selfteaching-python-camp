sample_text='''
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

# 1. 使用字典（dict 类型）统计字符串样本 text 中各个英文单词的出现次数

# 先将字符串根据 空白字符 分割成 list，要调用 str 类型
elements = sample_text.split()

# 定义一个新的 list 型变量，储存处理过的单词
words = []

# 先针对样本文本挑选出需要剔除的非单词符号
symbols = ',.*-!'

for element in elements:
    # 遍历一遍要剔除的符号
    for symbol in symbols:
        # 逐个替换字符号，用''是为了同时剔除符号所占的位置
        element = element.replace(symbol, '')
    # 剔除了字符后如果 element 的 长度不为 0，则算作正常单词
    if len(element):
        words.append(element)

print('正常的英文单词 ==>', words)

# 初始化一个 dict (字典)类型的变量，用来存放单词出现的次数
counter = {}

# set (集合) 类型 可以去掉 列表 里的重复元素，可以在 for...in 里减少循环次数
word_set = set(words)

for word in word_set:
    counter[word] = words.count(word)

print('英文单词出现的次数 ==>', counter)

# 2. 按照出现次数从大到小输出所有的单词及出现的次数

# 内置函数 sorted 的参数 key 表述按元素的那一项的值进行排序
# dict 类型 counter 的 items 方法会返回一个 包含 相应 项 (key, value) 的 元组 列表
print('从大到小输出所有的单词及出现的次数 ==>', sorted(counter.items(), key=lambda x: x[1], reverse=True))

