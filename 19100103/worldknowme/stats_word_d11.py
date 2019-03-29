#-*- coding:utf-8 -*-
# -*- coding:gbk -*-
import io
import sys
import re
import collections
from collections import Counter               
import jieba
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


   
def stats_text_en(stri,count):
    '''【NOTE】：The "stats_text_en()" is importing output result of English words and occurrences): ''' 
    try:
        if type(stri) != str:
            raise ValueError(stri)
    except ValueError as error:
        print(type(error))
        print("This data is not a string!")
    else:
        endict={}               #新建一个字典
        entext=""               #新建一个空字符串
        
        
        stri=stri.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')  #去标点
        
        #遍历原始字符串
        for i in stri: 
            if i.isascii():         #去掉中文或者说非英文字符  
                entext=entext+i     #将英文字符放入新建的字符串中

        entext=entext.split( )      #分隔字符串

        for i in entext:            #遍历新字符串
            endict[i]=entext.count(i)        #创建字典
    #    endict=sorted(endict.items(),key=lambda item:item[1],reverse=True) #按照值排序，从小到大
        endict = collections.Counter(endict).most_common(count)         #使用collection的counter方法，按照词频进行排序
        print(stats_text_en. __doc__) 
        print(endict)
        return endict

def stats_text_cn(stri,count):  
    '''【注】:stats_text_cn()函数为每个汉字统计的次数如下： '''  
    if type(stri) != str:
     raise ValueError("This is not string!")
    dictionary={}                                      
    entext2=""              
    for i in stri:
     if u'\u4e00' <= i <= u'\u9fa5':                    
        entext2=entext2+i  
    
    #筛选长度大于2的汉字：
    seg_list=jieba.cut(entext2,cut_all=False,HMM=False)
    string = "/".join(seg_list)
    string = string.split("/")
    for i in string:
      if len(i) >= 2:
         dictionary[i] = string.count(i)
    dictionary = collections.Counter(dictionary).most_common(count)
    print(stats_text_cn. __doc__) 
    print(dictionary)
    return dictionary
   

def stats_text(stri,count):            #定义stats_text函数
    if type(stri) != str:
     raise ValueError("This is not string!")
    '''注释:

    该函数的功能为：
    调用了两个函数：stats_text_cn(str)和stats_text_cn(str)
    作用是分别统计了英文单词出现的次数，以及中文词组（2字以上）出现的次数：
    '''
    print(stats_text.__doc__)     #输出注释，注意：__doc__中的下划线'__'需要键盘打两次'_'
    stats_text_en(stri,count)          
    stats_text_cn(stri,count)   
    return stats_text_cn(stri,count)+stats_text_en(stri,count)   #给函数一个return