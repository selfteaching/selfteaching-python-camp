

import re  
import collections #引入正则表达式
count = int()
def stats_text_en(en,count):        #定义一个函数
    #\u4e00-\u9fa5 	汉字的unicode范围
    #\u0030-\u0039 	数字的unicode范围
    #\u0041-\u005a 	大写字母unicode范围
    #\u0061-\u007a 	小写字母unicode范围
    #sub(pattern,repl,string) 	把字符串中的所有匹配表达式pattern中的地方替换成repl
    
    if  isinstance(en,str):
        t1= re.sub(u"([^\u0041-\u005a\u0061-\u007a])"," ",en) #将en中非英文字符转换成“ ”
        text1 = t1.split() #将字符串分割
        d = collections.Counter(text1).most_common(count)  #counter 函数自带统计排列功能
        return d
    else:
        raise ValueError("请输入字符串")


import jieba
def stats_text_cn(cn,count): #定义一个统计中文汉字字频的函数
    if isinstance(cn,str):
        t = re.sub(u"([^\u4e00-\u9fa5])","",cn)   #将cn中非中文字符转换成“”
        t1 = jieba.cut(t)
        t2 = []
        for i in t1:
            if len(i) >= 2:
                t2.append(i)
                d = collections.Counter(t2).most_common(count)
        return d
    else:
        raise ValueError("请输入字符串")


def stats_text(j,count): #定义合并输出函数
    a = stats_text_cn(j,count) + stats_text_en(j,count)  #将两次统计结果合并
    return a
