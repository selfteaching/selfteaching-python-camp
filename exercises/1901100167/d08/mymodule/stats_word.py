def stats_text_en(st1):
    if isinstance(st1,str):
        map=str.maketrans('*-.','   ')
        st1=st1.translate(map)
        a=st1.split()
        dic={}
        b=[]
        for x in a:
            if u'\u0041'<x<u'\u007a':
                dic.setdefault(x,0)
                dic[x]+=1
            b=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        return b
    else:
        raise TypeError

def stats_text_cn(st2):
        if isinstance(st2,str):
                a=list(st2)
                dic={} 
                b=[]
                for x in a:
                        if u'\u4e00'<x<u'\u9fa5':
                                dic.setdefault(x,0)
                                dic[x]+=1
                b=sorted(dic.items(),key=lambda x:x[1],reverse=True)
                return b
        else:
                raise TypeError

def stats_text(stri):
        if isinstance(stri,str):
                return stats_text_cn(stri)+stats_text_en(stri)
        else:
                raise TypeError