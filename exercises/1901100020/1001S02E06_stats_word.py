# 定义text这个字符串
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
# 1. 封装统计英⽂文单词词频的函数
# 定义一个名为 stats_text_en 的函数，函数接受一个字符串 text 作为参数
print()
def stats_text_en(text):
# 为 stats_text_en 添加注释说明
    """
    这是一个统计样本text中各个英文单词出现次数的函数
    """
# 实现该函数的功能（同 day5 任务 2）：统计参数中每个英⽂文单词出现的次数，最后返回一个按词频降序排列的数组
# 使⽤用字典（dict）统计字符串串样本 text 中各个英⽂文单词出现的次数。
elements = sample_text.split()
words = []
symbols= ',.*-!'
for element in elements:
    for symbol in symbols:
        element = element.replace(symbol,'')
    if len(element):
        words.append(element)
print('正常的英文单词 ==>',words)
print()
print()
counter = {}
word_set = set(words)
for word in word_set:
    counter[word] = words.count(word)
print("英文单词出现的次数 ==>",counter)
print()
print()
print('从大到小输出所有的单词及出现的次数 ==>', sorted(counter.items(), key=lambda x: x[1], reverse=True))
print()
print()
print()
help(stats_text_en)
print()

# 2. 封装统计中⽂文汉字字频的函数
sample_text  = '''中国中国天下只有两种人。比如一串葡萄到手，一种人挑最好的先吃，另一种人把最好的留到最后吃。照例第一种人应该乐观，因为他每吃一颗都是吃剩的葡萄里最好的；第二种人应该悲观，因为他每吃一颗都是吃剩的葡萄里最坏的。不过事实却适得其反，缘故是第二种人还有希望，第一种人只有回忆。'''

def stats_text_cn(text):
    """
    这是一个统计样本text中各个中文汉字出现次数的函数
    """
elements = sample_text.split()
words = [] # 这里的word是汉字
symbols= '。，；' # 这里的symbols是标点符号
for element in elements:
    
    # 统计以及删除标点符号symbols
    for symbol in symbols:
        element = element.replace(symbol,'')
    ## 之前一直缺一行这样的代码，即保留输出words中所有的重复性汉字
    for word in element:
        words.append(word)

    # 统计并保留汉字word
    for word in range(0,len(element)):
        # 如果字符第一次出现 加入到字符数组中
        if not element[word] in words:
            words.append(element[word])
        # 如果是字符第一次出现 加入到字典中
        elif element[word] not in counter:
            counter[element[word]] = 1

print('正常的中文汉字 ==>',words)
print()
print()
counter = {}
word_set = set(words)
for word in word_set:
    counter[word] = words.count(word)
print("中文汉字出现的次数 ==>",counter)
print()
print()
print('从大到小输出所有的汉字及出现的次数 ==>', sorted(counter.items(), key=lambda x: x[1], reverse=True))
print()
print()
print()
help(stats_text_cn)
print()