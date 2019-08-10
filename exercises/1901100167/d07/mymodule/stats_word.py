def stats_text_en(st1):
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
        return stats_text_cn(stri)+stats_text_en(stri)