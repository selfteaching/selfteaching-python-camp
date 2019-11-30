def stats_test_en(s):
    '''
    封装统计英文单词词频的函数'''
    i=s.split()
    b=[]
    d=',.*!-'
    for e in i:
        for f in d:
            e=e.replace(f,'')
        if len(e):
            b.append(e)
    g={}
    b_set=set(b)
    for h in b_set:
        g[h]=b.count(h)
    print(g)
    print(sorted(g.items(),key=lambda x: x[1],reverse=True)
help(stats_test_en)

def stats_test_cn(y)
    '''
    封装统计中文单词词频的函数'''
    j=y.split()
    c=[]
    q='，。*！-'
    for u in j:
        for p in q:
            k=k.replace(p,'')
        if len(u):
        c.append(u)
    n={}
    c_set=set(c)
    for v in c_set:
        k[v]=c.count(v)
    print(k)
    print(sorted(k.items(),key=lambda x: x[1],reverse=True)