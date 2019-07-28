


import re
def stats_text_en(en):
    if isinstance(en,str):
        d = {}
        t1 = re.sub(u"([^\u0041-\u005a\u0061-\u007a\'])"," ",en)
        t2 = t1.split()
        for i in t2:
            j=t2.count(i)
            d1={i:j}
            d.update(d1)
        d3=sorted(d.items(),key=lambda x:x[1],reverse = True)
        return d3
    else:
        raise ValueError ("输入的不是文本，请重新输入")
def stats_text_cn(cn):
    if isinstance(cn,str):
        d={}
        t1=re.sub(u"([^\u4e00-\u9fa5])","",cn)
        for i in t1:
            j=t1.count(i)
            d1={i:j}
            d.update(d1)
        d2=sorted(d.items(),key=lambda x:x[1],reverse=True)
        return d2
    else:
        raise ValueError("输入的不是文本，请重新输入")
def stats_text(ec):                                                   #创建stats_text函数
    if isinstance(ec,str):                                            #如果ec是字符串，则运行下面一行的代码。
        return stats_text_cn(ec) + stats_text_en(ec)                  #返回值为stats_text_cn(ec)和stats_text_en(ec)的结果。
    else:                                                              #否则提示错误：输入的不是文本。。。。。。
        raise ValueError ("输入的不是文本，请重新输入")