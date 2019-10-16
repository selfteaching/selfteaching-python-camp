


import re
import collections
def stats_text_en(en,count):
    if isinstance(en,str):
        d = {}
        t1 = re.sub(u"([^\u0041-\u005a\u0061-\u007a\'])"," ",en)
        t2 = t1.split()
        d=collections.Counter(t2).most_common(count)
        return d
    else:
        raise ValueError ("输入的不是文本，请重新输入")
def stats_text_cn(cn,count):
    if isinstance(cn,str):
        d={}
        t1=re.sub(u"([^\u4e00-\u9fa5])","",cn)
        d=collections.Counter(t1).most_common(count)
        return d
    else:
        raise ValueError("输入的不是文本，请重新输入")
def stats_text(ec,count):                                                   #创建stats_text函数
    if isinstance(ec,str):                                            #如果ec是字符串，则运行下面一行的代码。
        return stats_text_cn(ec,count) + stats_text_en(ec,count)                  #返回值为stats_text_cn(ec)和stats_text_en(ec)的结果。
    else:                                                              #否则提示错误：输入的不是文本。。。。。。
        raise ValueError ("输入的不是文本，请重新输入")