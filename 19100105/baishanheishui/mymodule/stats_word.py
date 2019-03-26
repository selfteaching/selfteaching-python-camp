#-*- coding:utf-8 -*-
import io
import sys
from collections import Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#文档字符串
def my_notes():
     """
     
     001 05   come on!

     """
     pass

#统计英文词频的函数
def stats_text_en(c):  
   try:
      if not isinstance(c,str):
         raise ValueError(c)
   except ValueError as err:
         print('调用stats_text_en函数，参数类型错误',type(err))
         
   else:   
      
    c=c.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')#将非英文字符替换为空格
             
    t=""               #新建一个空字符串
    #遍历原始字符串
    for i in c: 
        if i.isascii():         #去掉中文或者说非英文字符
            t=t+i     #将英文字符放入新建的字符串中

    t=t.lower()#将所有英文字符改为小写
    t=t.split()#以空格拆分为独立的单词
   #用Count的方式
    cnt=Counter()
    count=10
    for i in t:  
        cnt[i]+=1
    print(cnt.most_common(count)) 

   #用字典的方式
    #zidian={}
    #for i in t:  #将字符串转换为字典
        #count=t.count(i)
        #r1={i:count}
        #zidian.update(r1)

    #zidian1=sorted(zidian.items(),key=lambda x:x[1],reverse=True) #按照单词出现次数，从大到小排序
    #return zidian1


#统计中文字频的函数
def stats_text_cn(t):   
   try:
      if not isinstance(t,str):
         raise ValueError(t)
   except ValueError as err:
         print('调用stats_text_cn函数，参数类型错误',type(err))
         
   else:     
     word_lst = []
     word_dict = {}
     exclude_str = "，。！？、（）【】<>《》=：+-*—“”…"
     cnt=Counter()
     count=10
     # 添加每一个字到列表中
     for i in t: 
        if u'\u4e00' <= i <= u'\u9fff':
            word_lst.append(i)
     # 用count统计每个字出现的个数，并排序
     for i in word_lst:
        if i not in exclude_str:
            cnt[i] += 1     
     print(cnt.most_common(count)) 

     # 用字典统计每个字出现的个数  
     #for i in word_lst:
        #if i not in exclude_str:
             #if i.strip() not in word_dict: # strip去除各种空白
                #word_dict[i] = 1
             #else:
                #word_dict[i] += 1 
     #word_dict = sorted(word_dict.items(), key=lambda x:x[1],  reverse=True) ##按照汉字出现次数，从大到小排序
     #return word_dict
 

def stats_text(t):
   try:
      if not isinstance(t,str):
         raise ValueError(t)
   except ValueError as err:
         print('调用stats_text函数，参数类型错误',type(err))
         
   else:
      stats_text_cn(t)
      stats_text_en(t)
      print(my_notes.__doc__)


