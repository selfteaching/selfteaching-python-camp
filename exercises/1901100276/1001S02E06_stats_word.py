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
def stats_text_en(text):   #定义函数
    a=text.replace('-','').replace('*','')  #把括号中的'-'替换成‘’，相当于删除
    d=a.split()   #分隔
    w={}    #创建空列表
    for i in d:
        c=d.count(i)  #统计d里面的单词次数
        n={i:c}
        w.update(n) #把n里的单词添加到w里
    m=sorted(w.items(),key=lambda x:x[1],reverse=True)#排序
    print(m)
stats_text_en(text)#调用函数
text='''
如 果 有 关 某 事 的 细 节 能 契 合 到 人 们 对 此 事 认 知 的 心 理 图 景 之 中
那 么 描 述 中 的 细 节 越 多
它 看 来 就 越 真 实
而 人 们 也 就 会 认 为 它 越 可 能 发 生 — — 尽 管 任 何 不 确 定 性 细 节 的 加 入
都 只 会 使 总 的 复 合 描 述 变 得 更 不 可 能
'''
def stats_text_cn(text):   #定义函数
    g=text.replace('-','').replace('*','')  #把括号中的'-'替换成‘’，相当于删除
    l=g.split()   #分隔
    m={}    #创建空列表
    for j in l:
        p=l.count(j)  #统计l里面的单词次数
        k={j:p}
        m.update(k) #把k里的单词添加到m里
    t=sorted(m.items(),key=lambda x:x[1],reverse=True)#排序
    print(t)
stats_text_cn(text)