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
自学是一门手艺，打磨自学手艺。
'''


import re
def stats_text_en(en):
    d = {}
    t1 = re.sub(u"([^\u0041-\u005a\u0061-\u007a\'])"," ",en)
    t2 = t1.split()
    for i in t2:
        j=t2.count(i)
        d1={i:j}
        d.update(d1)
    d3=sorted(d.items(),key=lambda x:x[1],reverse = True)
    return d3
print(stats_text_en(text))
def stats_text_cn(cn):
    d={}
    t1=re.sub(u"([^\u4e00-\u9fa5])","",cn)
    for i in t1:
        j=t1.count(i)
        d1={i:j}
        d.update(d1)
    d2=sorted(d.items(),key=lambda x:x[1],reverse=True)
    return d2
print(stats_text_cn(text))
def stats_text(ec):                                               #创建stats_text函数
    return stats_text_cn(ec) + stats_text_en(ec)                  #返回值为stats_text_cn(ec)和stats_text_en(ec)的结果。
print(stats_text(text))