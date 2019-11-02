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

def stats_text_en(str):
    # 1. 使用字典（dict 类型）统计字符串样本 text 中各个英文单词出现的次数
    # 先将字符串根据 空白字符 分割成 list，要调用 str 类型
    # 定义一个新的 list 型变量，储存处理过的单词
    # 先针对样本文本挑选出需要剔除的非单词符号    
    elements = text.split()
    words = []
    symbols = ',.*-!'

    # 遍历一遍要剔除的符号
    # 逐个替换字符号，用 '' 是为了同时剔除符号所占的位置
    # 剔除了字符后如果 element 的长度不为0，则算作正常单词
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol, '')
        if len(element):
            words.append(element)

    #print('\n\n正常的英文单词 ==>', words)

    # 初始化一个 dict（字典）类型的变量，用来存放单词出现的次数
    # set（集合）类型 可以去掉 列表 里的重复元素，可以在 for...in 里减少循环次数
    counter = {}
    word_set = set(words)

    for word in word_set:
        counter[word] = words.count(word)

    #print('\n\n英文单词出现的次数 ==>', counter)

    # 2. 按照出现次数从大到小输出所有的单词及出现的次数

    # 内置函数 sorted 的参数 key 表示按元素的那一项的值进行排序
    # dict 类型 counter 的 items 方法会返回一个包含相应项（key，value）的 元组 列表
    result_sorted = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    print('这是英文单词降序输出==>\n')
    return result_sorted

print(stats_text_en(text))


text = '''
现在开始，不管是参与者招募、定向邀请、还是签到验票，在线抽奖，甚至是定制一套活动邀请函，所有的数据，都在同一平台。 
31 种字段类型，帮助你设计各种类型的问卷调研。 利用字段之间的逻辑跳转，整理更清晰的调研路径。专业的报表和数据导出，让你可以进一步分析样本价值。 
'''

import re
def stats_text_cn(str):
    x = ''.join(re.findall(u'[\u4e00-\u9fa5]+', text)) #正则表达式，汉字的编码范围进行匹配
    dict_list = {}
    for i in range(len(x)):
        if dict_list.get(x[i]):
            dict_list[x[i]] = dict_list[x[i]] + 1 #当i=0时，取得是list集合中第一个元素，当i=1时，取得是list集合中第二个元素，以此类推
        else:
            dict_list[x[i]] = 1
    #print(dict_list)
    result_sorted = sorted(dict_list.items(), key=lambda x: x[1], reverse=True) #进行降序排序
    print('这是中文单词降序输出==>\n')
    return result_sorted

print(stats_text_cn(text))