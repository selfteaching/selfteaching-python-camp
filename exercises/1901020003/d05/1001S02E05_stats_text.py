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
 Namespaces are one honking great idea -- let's do more of those!
 '''

 # 1. 使用字典 (dic 类型) 统计字符串样板 text 中各个英文单词出现的次数

 # 先将字符串根据 空白字符 分割成 list, 要调用 str 类型
elements = sample_text.split()

 # 定义一个新的 list 型变量,存储处理过的单词
word = []

 # 先针对样本文本挑选出来需剔除的非单词符号
symbols = ',.*-!'

for element in elements:
    # 遍历一遍要剔除的符号
    for symbols in symbols:
        # 逐个替换字符号，用  '' 是为了同时删除符号所占的位置
        element = element.replace(symbols, '')
# 剔除字符如果 element 的 长度不为 0, 则算正常单词
if len(element):
    word.append(element)

print('正常英文单词 ==>', word)

# 初始化一个 dic(字典) 类型的变量，用来存放单词出现的次数
counter = {}

# set (集合) 类型 可以去掉 列表 里的重复元素，可以在 for...in 里减少循环次数
word_set = set(word)

for word in word_set:
    counter[word] = word.count(word)

print('英文单词出现次数 ==>', counter)

# 2. 安装出现次数从大道小输出所有单词出现次数

# 内置函数 sortd 的参数 key 表示按元素的那一项值进行排序
# dic 类型 counter 的 items 方法会返回一个 包含 相应 项(key, value) 的 元组 列表
# print('counter.items() ==>' countered.items())
# print('从大到小输出所有单词及出现的次数 ==>', sorted(counter.items(), key=lambda x: x[1] reverse=True))
