#！/usr/bin/python
#-*-coding:UTF-8 -*-
#统计封装英文单词词频的函数，接受字符串，词频降序排列数组

import re #引入正则表达式，以便操作字串符，import放在最上方

text='''
The Zen of Python, by Tim Peters, 
Beautiful is better than ugly. 
Simple is better than Complex! 
Complex is better than complicated, 
Flat is better than nested. 
Readability counts.
Now is better than never.
信息高速公路的崛起，
知识经济的到来，
虚拟现实的出现，
人们才意识到他是对的他所谓的意识延伸就是赛博空间，
地球村真的已经到来！
媒体是人体的延伸，媒体就是信息，媒体有冷热之分，强调获得讯息的方式比讯息内容本身更来得重要，更有影响力。
并提出传播科技不仅可以引起人类感官能力变化更可以促进社会结构的变化，引发对于媒介科技的研究。 
'''

def stats_text_en(text): #定义函数
     pattern=re.compile("[a-zA-Z]+")
     result_list=re.findall(pattern,text)
     if not isinstance(text,str):
          raise ValueError("异常！输入的不是字符串")
     words=[]
     symbols=',.!。'
     for element in result_list:#element中集合的都是text文本中分割的文字，所有会有中英文都有的情况
          for symbol in symbols:

               element=element.replace(symbol,'')
          if len(element):
               words.append(element)
     counter_en={}
     word_set=set(words) #转换为set类型
     
     for word in word_set:
          counter_en[word]=words.count(word)
     return sorted(counter_en.items(),key=lambda x:x[1],reverse =True) #按单词出现的次数，降序排列

#统计封装中文汉字字频的函数
def stats_text_cn(text): #定义函数
     if not isinstance(text,str):
          raise ValueError("异常！输入的不是字符串")
     x=text.replace('。','').replace('！','').replace('，','') #去掉标点符号
     y=x.split()
     counter_cn={}
     for y in text:
          if '\u4c00'<=y<='\u9ffff': 
               if y not in counter_cn:
                    counter_cn[y]=1
               else:
                    counter_cn[y]+=1
     return sorted(counter_cn.items(),key=lambda x:x[1],reverse=True)

def stats_text(text):
     if not isinstance(text,str):
          raise ValueError("异常！输入的不是字符串")
     counter_en=stats_text_en(text)
     counter_cn=stats_text_cn(text)
     merge_counter=counter_en+counter_cn
     merge_counter=sorted(counter_en+counter_cn,key=lambda x:x[1],reverse=True)
     return merge_counter


if __name__=='__main__':
     counter_en=stats_text_en(text)
     counter_cn=stats_text_cn(text)
     merge_counter=stats_text(text)
     print('统计参数中每个英文单词出现的次数 ==>\n',counter_en)
     print('统计参数中每个中文汉字出现的次数 ==>\n',counter_cn)
     print('统计参数中每个中英文出现的次数==>\n',merge_counter)

