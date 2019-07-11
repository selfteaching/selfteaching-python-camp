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

# 使⽤字典（dict）统计字符串样本 text 中各个英⽂单词出现的次数
elements = text.split() #分割text文本
words = [] #构建空列表，[]→代表list列表数据类型，
symbols = ',.*-!' #为了只统计英文单词
for element in elements:
#<<<<<<< master
    for symbol in symbols:#symbol→符号的意思
#=======
    for symbol in symbols:
#>>>>>>> master
        element = element.replace(symbol,' ')#element.replace(old, new) →是吧所有的符号全部转换成''，也就是去掉所有符号
    if len(element): #用len()方法返回列表元素个数?长度？
        words.append(element) #更新后的word列表
print('正常的英文单词 ==>',words) #打印更改过后的字符串文本text
counter = {}#创建空字典  counter用于追踪值的出现次数  {}→代表dict字典数据类型
word_set = set(words)#创建集合
for word in word_set:
    counter[word] = words.count(word)#count()方法来统计word字符列表里单词出现的次数
print('英文单词出现的次数 ==>',counter)

#从⼤到⼩输出所有的单词及出现的次数
#<<<<<<< master
print('从大到小输出所有单词及出现的次数 ==>',sorted(counter.items(),key=lambda x: x[1],reverse=True))
#用sorted()函数对所有可迭代的对象进行排序操作，以下格式是固定写法
# ke*y=lambda x : x[1] 中的x可以是任何字母，[]中的数字是，相对元素第几个字段排序时，就写几
# 比如第一位 →[0]，第二位[1]...     reverse = True 降序 ， reverse = False 升序（默认）
       
#=======
print('从大到小输出所有单词及出现的次数 ==>',
#用sorted()函数对所有可迭代的对象进行排序操作，以下格式是固定写法
# ke*y=lambda x : x[1] 中的x可以是任何字母，[]中的数字是，相对元素第几个字段排序时，就写几
# 比如第一位 →[0]，第二位[1]...     reverse = True 降序 ， reverse = False 升序（默认）
       sorted(counter.items(),key=lambda x: x[1],reverse=True))
#>>>>>>> master



