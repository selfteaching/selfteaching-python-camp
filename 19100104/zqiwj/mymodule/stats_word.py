text_en = 1

import collections
import re
import jieba

def stats_text_en(text_en):
    if not isinstance(text_en,str):
        raise ValueError('不是字符串类型(string)!')
    result = re.sub("[^A-Za-z]", " ", text_en.strip())
    newList = result.split( )
    # i=0
    for i in range(0,len(newList)):
        newList[i]=newList[i].strip('*-,.?!')
        if newList[i]==' ': 
            newList[i].remove(' ')
        else:
            i=i+1
    print('英文单词词频统计结果： ',collections.Counter(newList).most_common(10) )


def stats_text_cn(text_cn):
    if not isinstance(text_cn,str):
        raise ValueError('不是字符串类型(string)!')
    result1 = re.findall(u'[\u4e00-\u9fff]+',text_cn)
    newString = ''.join(result1)
    seg_list = jieba.cut(newString, cut_all=False)
    f = list(seg_list)
    a = []
    for i in range(len(f)):
        if len(f[i]) > 1:
            a.append(f[i])
        else:
            continue
    print('中文汉字字频统计结果： ', collections.Counter(a).most_common(20))

def stats_text(text):
    if not isinstance(text,str):
        raise ValueError('不是字符串类型(string)!')
    stats_text_en(text)
    stats_text_cn(text)

# 以下为调试函数用
# stats_text_en(text)
# stats_text_cn(text)