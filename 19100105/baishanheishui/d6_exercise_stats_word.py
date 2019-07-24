#-*- coding:utf-8 -*-

text1 = '''
又有谁不想解决掉焦虑呢？又有谁不想马上解决掉焦虑呢？
于是，你焦虑，你就要找解决方案。而焦虑的你找到的解决方案，就是花个钱买本书，报个班，找个老师，上个课
这能说是别人贩卖焦虑给你吗？
自学能力强的人，并非不花钱，甚至他们花的钱可能更多。他们也花钱买书，而且买更多的书；他们也可能花钱上课，而且要上就上
最好的课、最好的班；他们更经常费尽周折找到恰当的人咨询、求教、探讨
所以，事实上，他们更可能花了更多的钱。
但，自学能力强的人不焦虑，起码他们不会因为学习以及学习过程而焦虑。这是重大差别。
而焦虑的大多数，并不是因为别人贩卖焦虑给他们他们才“拥有”那些焦虑。他们一直在焦虑，并且越来越焦虑。
'''

text2 = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
#文档字符串
def my_notes():
     """
     
     001 05   come on!

     """
     pass

#统计英文词频的函数
def stats_text_en(text):  
    text=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')#将非英文字符替换为空格
    text=text.lower()#将所有英文字符改为小写
    text=text.split()#以空格拆分为独立的单词
    zidian={}
    for i in text:  #将字符串转换为字典
        count=text.count(i)
        r1={i:count}
        zidian.update(r1)

    zidian1=sorted(zidian.items(),key=lambda x:x[1],reverse=True) #按照单词出现次数，从大到小排序
    return zidian1

stats_text_en(text2) 
print(my_notes.__doc__)




#统计中文字频的函数
def stats_text_cn(t):   
     word_lst = []
     word_dict = {}
     exclude_str = "，。！？、（）【】<>《》=：+-*—“”…"
     # 添加每一个字到列表中
     for i in t: 
        word_lst.append(i)
     # 用字典统计每个字出现的个数  
     for i in word_lst:
        if i not in exclude_str:
             if i.strip() not in word_dict: # strip去除各种空白
                word_dict[i] = 1
             else:
                word_dict[i] += 1 
     word_dict = sorted(word_dict.items(), key=lambda x:x[1],  reverse=True) ##按照汉字出现次数，从大到小排序
     return word_dict
 

stats_text_cn(text1)
print(my_notes.__doc__)


