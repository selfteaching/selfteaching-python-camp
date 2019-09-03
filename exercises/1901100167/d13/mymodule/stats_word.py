import jieba
def stats_text_en(st1):
    if not isinstance(st1,str):
        raise TypeError('must be string,yours is %s type'%type(st1))               
    else:
        from collections import Counter
        map=str.maketrans('*-.','   ')
        st1=st1.translate(map)
        a=jieba.cut(st1)
        c= Counter()
        for x in a:
            if u'\u0041'<x<u'\u007a':
                c.setdefault(x,0)
                c[x]+=1
        count=c.most_common(100)
        return count

def stats_text_cn(st2):
    if not isinstance(st2,str):
        raise TypeError('must be string,yours is %s type'%type(st2))
    else:
        from collections import Counter
        a=jieba.cut(st2)
        c=Counter()
        for x in a:
            if u'\u4e00'<x<u'\u9fa5' and len(x)>=2:
                c.setdefault(x,0)
                c[x]+=1
        count=c.most_common(10)
        return count
        

def stats_text(stri):
    if not isinstance(stri,str):
        raise TypeError('must be string,yours is %s type'%type(stri))
    else:
        return stats_text_cn(stri)+stats_text_en(stri)