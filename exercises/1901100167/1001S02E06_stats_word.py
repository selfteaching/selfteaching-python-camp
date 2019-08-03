text = r'''The Zen of Python, by Tim Peters
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
Namespaces are one honking great idea -- let's do more of those .
'''

text2='''
深啡网烦无法是而是艾弗森额额，。234 qewffesaf
'''
def stats_text_en(st1):
        map=str.maketrans('*-.','   ')
        st1=st1.translate(map)
        a=st1.split()
        dic={}
        b=[]
        for x in a:
                dic.setdefault(x,0)
                dic[x]+=1
        b=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        return b

print(stats_text_en(text))

def stats_text_cn(st2):
        a=list(st2)
        dic={}
        b=[]
        for x in a:
                if u'\u4e00'<=x<=u'\u9fa5':
                        dic.setdefault(x,0)
                        dic[x]+=1
        b=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        return b

print(stats_text_cn(text2))

