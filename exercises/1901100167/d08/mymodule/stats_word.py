def stats_text_en(st1):
    if not isinstance(st1,str):
        raise TypeError('must be string,yours is %s type'%type(st1))               
    else:
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

def stats_text_cn(st2):
    if not isinstance(st2,str):
        raise TypeError('must be string,yours is %s type'%type(st2))
    else:        
        a=list(st2)
        dic={} 
        b=[]
        for x in a:
            if u'\u4e00'<x<u'\u9fa5':
                dic.setdefault(x,0)
                dic[x]+=1
        b=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        return b

def stats_text(stri):
    if not isinstance(stri,str):
        raise TypeError('must be string,yours is %s type'%type(stri))
    else:
        return stats_text_cn(stri)+stats_text_en(stri)