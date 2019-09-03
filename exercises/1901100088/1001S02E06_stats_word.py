text_en='''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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

text_cn="""
优美胜于丑陋
明了胜于晦涩
简洁胜于复杂
复杂胜于凌乱
扁平胜于嵌套
间隔胜于紧凑
可读性很重要
即便假借特例的实用性之名，也不可违背这些规则
"""


def stats_text_en(text):
    """Calculate the occurrence number of the english word.
    """

def stats_text_en(text)-> str:
    """Calculate the occurrence number of the english word.
    """
    print("Annotations:", stats_text_en.__annotations__)

    stat = text.lower()
    stats = stat.split()
    word = []
    puns= ',.*-!9'
    for s in stats:
        for pun in puns:
            if pun in s:
                s = s.replace(pun,"")
        if len(s):
                word.append(s)
    count_word = []
    for cw in word:
        count_word.append(word.count(cw))
    dic = dict(zip(word,count_word))
    stat_en = sorted(dic.items(),key=lambda item:item[1], reverse=True)
    print(stat_en)

stats_text_en(text_en)

def stats_text_cn(text):
    """Calculate the occurrence number of the chinese word.
    """
    
    text_c = []
    for d in text:
        text_c.append(d)
    cw = []
    for c in text_c:
        cw.append(text_c.count(c))
    dic = dict(zip(text_c,cw))
    dic.pop("，")
    dic.pop("\n")
    stat_cn = sorted(dic.items(),key=lambda item:item[1], reverse=True)
    print(stat_cn)

stats_text_cn(text_cn)

