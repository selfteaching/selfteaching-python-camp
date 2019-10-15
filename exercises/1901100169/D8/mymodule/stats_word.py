# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:43:52 2019

"""

#text=input('请输入英文:\n')
def stats_text_en(text):
    if text.isascii() and text.isdigit()==0:
        x='*-,.!@#$%^&()_\?><=+' #列出要替换的标点符号
        words_dict={} #空字典
        for c in x: #按每个标点在X里面循环
            text=(text.replace(c,'')) #重置的text的值
        words=text.lower().split() #将text小写字母化后切片给words赋值
        b=set(words) #将words去掉重复项赋值给B
        for word in b: #在B里的每个单词循环
            d=words.count(word) #计算每个单词在words里出现的次数，赋值给D
            words_dict[word]=d #每个单词及出现的次数以字典的方式存储在words_dict
        e=sorted(words_dict.items(),key=lambda t:t[1],reverse=True) #将字典里的项目按值的大小降序排列
        print(e) #打印E
    else: 
        raise ValueError#('请输入正确英文文本')
    return
#stats_text_en(text)

#text1=input('请输入中文:\n')
def stats_text_cn  (text1): #定义函数stats_text_cn    
    if text1 >= u'\u4e00' and text1<=u'\u9fa5':
        import re               #导入模块
        i=r"[\u4e00-\u9fa5]"    #unicode代码库
        j= re.compile(i)        #将创建的模式对像赋值给J
        k= re.findall(j,text1)  #将与模式与文本匹配得到的unicode代码赋值给K
        dict={}                 #建空字典
        for l in k:             #在K内每个字循环
            m=k.count(l)        #计算每个字K里出现的次数赋值给M
            dict[l]=m           #将每一项存入字典
        q=sorted(dict.items(),key=lambda y:y[1],reverse=True) #字典项按出现次数降序
        print(q)                #打印排序后的结果
    else: 
        raise ValueError#('请输入正确中文文本')
    return                    #返回
#stats_text_cn(text1)       
def stats_text():
    z=stats_text_en(text)
    v=stats_text_cn(text1)
    return

 
    