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
from collections import Counter
import jieba
def stats_text_en(text,Count):   #定义函数
    if not isinstance(text,str):
        raise ValueError('字符串必须是str类型')
    a=text.replace('-','').replace('*','')  #把括号中的'-'替换成‘’，相当于删除
    d=a.split()   #分隔
    w={}    #创建空列表
    for i in d:
        c=d.count(i)  #统计d里面的单词次数
        n={i:c}
        w.update(n) #把n里的单词添加到w里
#m=sorted(w.items(),key=lambda x:x[1],reverse=True)#排序
    #return m
    return Counter(w).most_common(Count)
#stats_text_en(text,Count)#调用函数
text='''
如 果 有 关 某 事 的 细 节 能 契 合 到 人 们 对 此 事 认 知 的 心 理 图 景 之 中
那 么 描 述 中 的 细 节 越 多
它 看 来 就 越 真 实
而 人 们 也 就 会 认 为 它 越 可 能 发 生 — — 尽 管 任 何 不 确 定 性 细 节 的 加 入
都 只 会 使 总 的 复 合 描 述 变 得 更 不 可 能
'''
def stats_text_cn(text,Count):   #定义函数
    if not isinstance(text,str):    #引发异常
        raise ValueError('字符串必须是str类型' ) 
    #g=text.replace('-','').replace('*','')      #把括号中的'-'替换成‘’，相当于删除
    seg_list=jieba.cut(text)
    print("Default Mode: " + "/ ".join(seg_list))
    m=[]    #创建空列表
    for j in seg_list :
        if len(j)>1:    #判断单词长度是否大于1
            m.append(j)     #将分词过的单词j添加到m列表中
    #t=sorted(m.items(),key=lambda x:x[1],reverse=True)  #排序
    #return t
    return Counter(m).most_common(Count)    #排序
#stats_text_cn(text,20)
def stats_text(text,Count):   #合并词频统计结果
    if not isinstance(text,str):    #引发异常
        raise ValueError('字符串必须是str类型')
    return stats_text_en(text,Count) + stats_text_cn(text,Count)
#stats_text_cn(1)#验证参数检查功能是否⽣效




