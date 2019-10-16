from inspect import signature
from functools import wraps

def typeassert(type_args,str):
    if not isinstance(type_args,str):
        raise ValueError



def stats_text_en(text):
    typeassert(text,str)
    text=text.replace(',',' ').replace('.',' ').replace('--','')
    text=text.lower()
    text=text.split()
    zidian={}
    for i in text:
        count=text.count(i)
        r1={i:count}
        zidian.update(r1)
        print(zidian)

        zidian1=sorted(zidian.items(),key=lambda x:x[1],reverse=True)
        print(zidian1)



import re
def stats_text_cn(text):
    typeassert(text,str)
    result1 = re.findall(u'[\u4e00-\u9fff])+',text)
    newString = ''.join(result1)
    b={}
    for i in result1:
        b.update({i:newString.count(i)})
    b1 = sorted(b.items(),key=lambda x:x[1],reverse=True)
    print('the result of counting chinese words ',b1,'\n')

def stats_text(text):
    typeassert(text,str) 
    stats_text_en(text)
    stats_text_cn(text)
