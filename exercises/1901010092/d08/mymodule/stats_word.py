import re

def stats_word_en(text):
    
    if type(text)==str:
        result=re.sub("[^A-Za-z]"," ",text.strip())
        newlist = result.split()
        a={}
        for i in newlist:
            a.update({i:newlist.count(i)})
        a1=sorted(a.items(),key=lambda e:e[1],reverse=True)
        return a1
    else:
        raise ValueError(type(text))

def stats_word_cn(text):
    if type(text)==str:
        result1 = re.findall(u'[\u4e00-\u9fff]', text)
        newstring = result1
        b={}
        for i in result1:
            b.update({i:newstring.count(i)})
        b1=sorted(b.items(),key=lambda x:x[1],reverse=True)
        return b1
    else:
        raise ValueError(type(text))
def stats_text(text):
    return(stats_word_en(text),stats_word_cn(text))



