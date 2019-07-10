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

text1='''自学是一门手艺，打磨自学手艺。'''


def stats_text_en(en):
    d = {}
    t1 = en.replace(','," ").replace('.',' ').replace('!',' ').replace('*',' ').replace('-',' ')
    t2 = t1.split()
    for i in t2:
        j=t2.count(i)
        d1={i:j}
        d.update(d1)
    d2=sorted(d.items(),key=lambda x:x[1],reverse = True)
    return d2
print(stats_text_en(text))
def stats_text_cn(cn):
    d={}
    t1=cn.replace('，','').replace('。','')
    for i in t1:
        j=t1.count(i)
        d1={i:j}
        d.update(d1)
    d2=sorted(d.items(),key=lambda x:x[1],reverse=True)
    return d2
print(stats_text_cn(text1))