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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
def stats_text_en(zen):
    a=text.split()
    b=',.-!*'
    c=[]
    for x in a:
        for y in b:
            x=x.replace(y,'')
        if len(x):
            c.append(x)
    # print(set(c))
    d={}
    e=set(c)
    for z in e:
        d[z]=c.count(z)
    return sorted(d.items(),key=lambda x: x[1],reverse=True)

if __name__=='__main__':
    f=stats_text_en(text)
    print('单词出现次数是：',f)

text='''
短歌行
作者：李白
白日何短短，百年苦易满。
苍穹浩茫茫，万劫太极长。
麻姑垂两鬓，一半已成霜。
天公见玉女，大笑亿千场。
吾欲揽六龙，回车挂扶桑。
北斗酌美酒，劝龙各一觞。
富贵非所愿，与人驻颜光。
'''
def stats_text_cn(libai):
    a=[]
    for b in text:
        if '\u4e00'<=b<='\u9fff':
            a.append(b)
    # print(a)
    c={}
    d=set(a)
    for x in d:
        c[x]=a.count(x)
    return sorted(c.items(),key=lambda x: x[1],reverse=True)

if __name__=='__main__':
    f=stats_text_cn(text)
    print('每个字出现次数是：',f)