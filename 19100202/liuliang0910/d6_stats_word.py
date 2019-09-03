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

# 6.1   英文降序统计字符
def stats_text_en(text):  # 统计英文词频
    a=text.split()        #把字符串变成列表
    import collections        #统计函数
    b=collections.Counter(a)
    return (b)                 #回旋值，重复定义的
print(stats_text_en(text))

# 6.2   中文降序统计字符

text2='''
    这是一张遗世独立的音乐专辑。
    难以想象会有一个新人竟然如此登场。
    在他身上似乎找不到任何模仿的踪迹，怪得自成一格。
    他不谈论爱情，也不评说时事。所有商业的、廉价的献媚他统统抛弃。
    他在讲着一些和你若即若离的故事，他着力塑造出优越的、压迫的，甚至是别扭的、好笑的感觉。
    到最后你或许不明所以，或许感到有些难过。总之这九首歌讲完了他要讲的。
    '''



def stats_text_cn(text2):  # 统计中文词频
    countcn={}
    for ch in text2:
        if u'\u4e00' <= ch <= u'\u9fff':
            countcn[ch] = text2.count(ch)
    countcn = sorted(countcn.items(), key=lambda item: item[1], reverse=True)  #按出现数字从大到小排列
    return countcn
print(stats_text_cn(text2))     #中文的确实不知道怎么弄，按照英文的方法，打不到，然后，抄了一遍高手的






