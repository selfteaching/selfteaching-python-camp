#-*- coding:utf-8 -*-
import io
import sys
import re
import collections
import jieba
import json
from collections import Counter               #引用 Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


def stats_text_en(stri,count):               #封装 d5_exercise_stats_text.py
    '''【NOTE】：The "stats_text_en()" is importing output result of English words and occurrences): ''' 
    if type(stri) != str:
         raise ValueError("This is not string!")
   # endict={}               #新建一个字典
    entext=""               #新建一个空字符串
    stri=stri.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')  #去标点
    #遍历原始字符串
    for i in stri: 
        if i.isascii():         #去掉中文或者说非英文字符
            entext=entext+i     #将英文字符放入新建的字符串中
    entext=entext.split( )      #分隔字符串
    cnt=Counter()

    for i in entext:  
     cnt[i]+=1
    print(stats_text_en. __doc__) 
    print(cnt.most_common(count)) 

def stats_text_cn1(stri,count):  
    '''【注】:stats_text_cn()函数为每个汉字统计的次数如下： '''  #用文档字符串注释
    if type(stri) != str:
        raise ValueError("This is not string!")

    dictionary={}                                       #引用一个空字典
    entext2=[]              
    for i in stri:
     if u'\u4e00' <= i <= u'\u9fa5':                    #提取中文汉字   \u是unincode编码，u4e00是十六进制表达值
         entext2.append(i)
    

    cnt=Counter()
   
    for i in entext2:  
        cnt[i]+=1  

    seg_list = jieba.cut(entext2,cut_all=False,HMM=False)
    entext3 = "/".join(seg_list)
    entext3=entext3.split("/")

    if i in entext3:
        if len(i)>=2:   
            dictionary[i]=entext3.count(i)
    dictionary = collections.Counter(dictionary).most_common(count) 
    print(stats_text_cn1. __doc__) 
    print(dictionary) 


def stats_text(stri,count):            #定义stats_text函数
    if type(stri) != str:
     raise ValueError("This is not string!")
    '''注释:
    该函数的功能为：
    调用了两个函数：stats_text_cn(str)和stats_text_cn(str)
    作用是分别统计了英文单词出现的次数，以及中文汉字出现的次数：
    '''
    print(stats_text.__doc__)     #输出注释，注意：__doc__中的下划线'__'需要键盘打两次'_'
    stats_text_en(stri,count)          
    stats_text_cn1(stri,count)   
    return stats_text_cn1(stri,count)+stats_text_en(stri,count)   #给函数一个return