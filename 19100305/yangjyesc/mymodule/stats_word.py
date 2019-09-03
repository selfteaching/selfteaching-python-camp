text='''

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
屈原 既放 ， 游于 江潭 ， 行吟 泽畔 ； 颜色 憔悴 ， 形容 枯槁 。 渔父 见而 问之 曰 ： “ 子非 三闾大夫 与？ 何故 至于斯 ？ ” 屈原 曰 ：“ 举世皆浊我独清，众人皆醉我独醒，是以见放。”
'''

def stats_text_en(text):
    """count the english words in the text"""
    counten={}
    for x in text:
        if x in text:
           counten[x]=text.count(x)
        else:
           counten[x]=text.count(x)+1
    return counten
print(sorted(stats_text_en(text.split()).items(),key=lambda item:item[1],reverse=True))

def stats_text_cn(text):
    """count the chinese words in the text"""
    countcn={}
    for i in text:
        if u'\u4e00'<=i<=u'\u9fff':
            countcn[i]=text.count(i)
        else:
            countcn[i]=text.count(i)+1
    return countcn
print(sorted(stats_text_cn(text).items(),key=lambda item:item[1],reverse=True))

def stats_text(text):
    return dict(stats_text_en(text),**stats_text_cn(text))
print(stats_text(text))