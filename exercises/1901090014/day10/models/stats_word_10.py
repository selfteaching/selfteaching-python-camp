from collections import Counter  # 引用库
import jieba

import re 

def stats_text_en(a,count):   #定义函数
    a=a.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
    a=a.split() # 切割字符串 
    if type(a) != str:                   #利用判断语句进行分析
        raise ValueError('valuerror:it is not string stats_text_en')
    number = Counter()
    for s in a:  # 只保留英文单词
        if s.isascii():
            number[s]+=1

    return Counter(number).most_common(count)  

#print(stats_text_en(a))  使用函数


def stats_text_cn(x,count): #定义函数
    j={}
    if type(x)!=str:                   #利用判断语句进行分析
        raise ValueError('valuerrorr:it is not string stats_text_en')   

    x=re.sub('[^\u4e00-\u9fa5]','',x)
    j=''.join(x)#将列表转换为字符串
    xu_a = jieba.cut(j, cut_all=False)
    number = []
    for e in xu_a :                    #通过循环统计汉字
        if len(e)>=2 :
            number.append(e)

    return Counter(number).most_common(count)

def stats_text(a,count):
    if type(a) !=str:                   #利用判断语句进行分析
        raise ValueError('valuerror:it is not string stats_text_en')
    print(stats_text_cn(a,count))  # 输出中文汉字字频
    print(stats_text_en(a,count)) # 输出英语单词词频



    