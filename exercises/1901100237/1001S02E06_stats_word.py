def stats_text_en(text):
    texts = text.split()
    aa = []
    c = '+, -， *, /, &, %, ?, !'
    for a in texts:
        for cc in c:
            a = a.replace(cc,'')
        if len(a):
            aa.append(a)
        d = {}
        z = set(aa)
    for v in z:
        d[v] = aa.count(v)
    # print('输出结果 ==>', sorted(d.items(), key=lambda x: x[1], reverse=True))
    return sorted(d.items(), key=lambda x: x[1], reverse=True)
    #将文本text中英文单词出现次数统计并按词频降序输出
from html.parser import HTMLParser
def stats_text_cn(text):
    texts = text.split()
    aa = []
    for a in texts:
        if len(a):
            aa.append(a)
        d = {}
        z = set(aa)
    for v in z:
        d[v] = aa.count(v)
    # print('输出结果 ==>', sorted(d.items(), key=lambda x: x[1], reverse=True))
    return sorted(d.items(), key=lambda x: x[1], reverse=True)
    
text_en = """
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
    """

text_cn = '''
    python之禅 by Tim Perers
    优美胜于丑陋
    明了胜于晦涩
    简洁胜于复杂
    复杂胜于凌乱
    扁平胜于嵌套
    间隔胜于紧凑
    可读性很重要
    即使假借特例的实用性之名，也不可违背这些规则
    不要包容所有错误，除非你确定需要这样做
    当存在多种可能，不要尝试去猜测
    而是尽量找一种，最好是唯一一种明显的解决方案
    显然这并不容易，因为你不是 Python 之父
    做也许好过不做，但不假思索就动手还不如不做
    。。。
    '''

print('输出结果cn ==>',stats_text_cn(text_cn))
print('输出结果en ==>',stats_text_cn(text_en))