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

elements=sample_text.split()#先将字符串根据空白字符分割成list，要调用str类型
words=[]#定义一个新的list型变量，存储处理过的单词
symbols=',.*-!'#针对文本筛选出需要剔除的非单词符号

for element in elements:
    for symbol in symbols:#遍一遍需要剔除的符号
        element=element.replace(symbol,'')#逐个替换字符号，用‘’是为了同时剔除符号所占的位置
    if len(element):
        words.append(element)#剔除了字符后如果element的长度不为0，则算作正常单词
print('',words)

counter = {}#初始化一个dict（字典）类型的变量，用来存放单词出现的次数
word_set = set(words)#set（集合）类型可以去掉列表里的重复元素
for word in word_set:
    counter[word] = word.count(word)
print('',counter)#在for··in里减少循环次数
print('',sorted(counter.items(),key=lambda x:x[1],reverse=True))
#按照出现次数从大到小输出所有的单词及出现次数
#内置函数sorted的参数key表示按元素的哪一项进行排序
#dict类型counter的items方法会返回一个包含相应项（key,value）的元素列表
#print('counter.items()‘，counter.items()）

sample_text = '''
The Zen of Python, by Tim Peters

美 丽 优 于 丑 陋.
直 言 优 于 暗 示.
简 单 优 于 复 杂.
复 杂 优 于 难 懂.
平 直 优 于 曲 折.
疏 散 优 于 密 集.
重 在 重 读.
打 破 规 则 的 特 别 不 能 称 之 为 特 别.
尽 管 练 习 会 打 败 纯 粹.
错 误 不 应 该 无 声 的 过 去.
除 非 明 晰 沉 默.
直 面 拒 绝 猜 测.
这 将 只 有 一 个-- 完 美 的 仅 有 的 --显 然 易 见 的 路 去 做.
尽 管 那 条 路 一 开 始 并 不 明 显 除 非 你 延 展.
现 在 好 过 从 不.
尽 管 从 不 常 好 过 *对 的* 现 在.
如 果 执 行 很 难 解 释，那 也 许 是 坏 点 子.
如 果 执 行 很 易 解 释，那 也 许 是 好 点 子.
命 名 空 间 是 最 棒 的 想 法 -- 让 我 们 做 的 更 多!
'''

elements=sample_text.split()#先将字符串根据空白字符分割成list，要调用str类型
words=[]#定义一个新的list型变量，存储处理过的单词
symbols=',.*-!'#针对文本筛选出需要剔除的非单词符号

for element in elements:
    for symbol in symbols:#遍一遍需要剔除的符号
        element=element.replace(symbol,'')#逐个替换字符号，用‘’是为了同时剔除符号所占的位置
    if len(element):
        words.append(element)#剔除了字符后如果element的长度不为0，则算作正常单词
print('',words)

counter = {}#初始化一个dict（字典）类型的变量，用来存放单词出现的次数
word_set = set(words)#set（集合）类型可以去掉列表里的重复元素
for word in word_set:
    counter[word] = word.count(word)
print('',counter)#在for··in里减少循环次数
print('',sorted(counter.items(),key=lambda x:x[1],reverse=True))
#按照出现次数从大到小输出所有的单词及出现次数
#内置函数sorted的参数key表示按元素的哪一项进行排序
#dict类型counter的items方法会返回一个包含相应项（key,value）的元素列表
#print('counter.items()‘，counter.items()）






