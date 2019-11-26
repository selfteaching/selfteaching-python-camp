sample_text = '''
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
Namespaces are on honking great idea -- let's do more of those!
'''

elements = sample_text.split() #字符串分割，返回单词列表

words = [] #新定义list，存放处理过的单词

symbols = ',.*-!' #选出要剔除的符号

#用循环剔除不需要的符号
for element in elements: #首先遍历符号是否在单词中
    for symbol in symbols: # 再遍历符号是否在剔除的富豪中
        element = element.replace(symbol, '') #替换，同时剔除符号的占位
    if len(element):  #判断element长度如不为0，则放入新定义的列表word中
        words.append(element)

print('正常的英文单词 ==>', words)

counter = {} #新定义字典类型变量，以存放单词出现的次数

word_set = set(words) #首先定义一个集合set类型，以去掉重复的元素（e.g. better, a），减少for in循环次数

for word in word_set:
    counter[word] =words.count(word) #对字典里的项进行赋值

print('英文单词出现的次数 ==>', counter)

# 按照出现次数，从大到小输出单词及次数

print('从大到小输出所有单词及出现的次数==>',sorted(counter.items(), key=lambda x: x[1], reverse=True))

# counter.items()会返回一个包含相应项(key, value)的元组列表
# 尝试print('counter.items()==>', counter.items())可见列表结果
# lambda后面直接跟变量，变量后是冒号，冒号后是表达式，表达式计算结果就是函数的返回值