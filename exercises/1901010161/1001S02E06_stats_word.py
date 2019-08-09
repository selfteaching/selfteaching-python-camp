import re    # 调用正则表达式


def stats_text_en(text):  # 定义英语文本统计函数
    m = re.sub(r'[^A-Za-z]', ' ', text)    # 将text中任意非字母成分替换为空
    str = m.split()        # 切分英文单词，建立字符串
    wordcount = {}         # 建立字典
    for i in str:
        wordcount[i] = str.count(i)
    wordcount = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)
    print(wordcount)
    return wordcount      # 原来这里只写了return，系统虽然没报错，但输出时结果最后面有个none，没明白错误出在哪里，经老师提醒改正后果然没有none了


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
《蟒蛇禅》，提姆•彼得斯著
美胜于丑。
显式优于隐式。
简单胜于复杂。
复杂总比复杂好。
平的比嵌套的好。
稀疏胜于稠密。
可读性计数。
特殊情况不足以打破规则。
尽管实用性胜过纯洁性。
错误永远不会悄悄地过去。
除非明确沉默。
面对悠闲，拒绝猜测的诱惑。
应该有一种——最好只有一种——显而易见的方法来做到这一点。
不过，如果不是荷兰语的话，这种方式一开始可能并不明显。
现在总比没有好。
虽然从来没有比现在更好。
如果实现很难解释，那是个坏主意。
如果实现很容易解释，这可能是一个好主意。
名称空间是一个非常好的主意——让我们做更多的事情吧！
'''
print(stats_text_en(text))


def stats_text_cn(text):     # 定义中文文本统计函数
    p = re.compile(r'[\u4e00-\u9fa5]')    # 中文基本汉字（20902字）的编码范围是：\u4e00到\u9fa5
    res = re.findall(p, text)   # 获取所有中文字符
    wordcount = {}
    for i in res:
        wordcount[i] = res.count(i)     # 词频统计词典设置
    wordcount = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)
    print(wordcount)  # 输出每个中文汉字频数统计结果
    return wordcount


print(stats_text_cn(text))
