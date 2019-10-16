#！/usr/bin/python
#-*-coding:UTF-8 -*-
#统计封装英文单词词频的函数，接受字符串，词频降序排列数组

import re #引入正则表达式，以便操作字串符，import放在最上方

def stats_text_en(text): #定义函数
     x=text.replace('.','').replace('!','').replace(',','') #去掉标点符号
     y=x.split() #拆分
     text_set=set(y) #转换为set类型
     counter={}  #用于存放单词和出现的次数
     for en in text_set: #从集合text_set取单词，在列表里统计出现的次数，然后存入字典里
          counter[en]=y.count(en) #向字典赋值
     counter_sort=sorted(counter.items(),key=lambda x:x[1],reverse =True) #按单词出现的次数，降序排列
     return counter_sort
a='The Zen of Python,by Tim Peters, Beautiful is better than ugly. Simple is better than Complex! Complex is better than complicated, Flat is better than nested. Readability counts. Now is better than never.' 
print(stats_text_en(a))


#统计封装中文汉字字频的函数

def stats_text_cn(text): #定义函数
     x=text.replace('。','').replace('！','').replace('，','') #去掉标点符号
     y=x.split()
     counter={}
     for y in text:
          if '\u4c00'<=y<='\u9ffff': 
               if y not in counter:
                    counter[y]=1
               else:
                    counter[y]+=1
     counter=sorted(counter.items(),key=lambda x:x[1],reverse=True)
     return counter
a='信息高速公路的崛起，知识经济的到来，虚拟现实的出现，人们才意识到他是对的他所谓的意识延伸就是赛博空间，地球村真的已经到来！媒体是人体的延伸，媒体就是信息，媒体有冷热之分，强调获得讯息的方式比讯息内容本身更来得重要，更有影响力。并提出传播科技不仅可以引起人类感官能力变化更可以促进社会结构的变化，引发对于媒介科技的研究。'
print(stats_text_cn(a))