# -*- coding: utf-8 -*-

text= '''
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
text1='''澎湃新闻9月26日从公安部交管局获悉，
    国庆假期全国将再次迎来自驾出行高峰，高速公路、景区周边道路交通压
    力和安全风险将显著增大。近日，公安部对近年来国庆假期道路交通事故
    情况进行分析，对今年国庆假期交通安全形势进行研判，并向社会公众发
    出交通安全预警。
    近三年国庆假期道路交通事故情况显示，小客车及高速公路是事故预防的
    重点车辆和重点道路。从导致死亡事故的原因看，未按规定让行、无证驾
    驶、超速行驶肇事最多，酒驾醉驾、超速行驶、未按规定让行肇事导致死
    亡人数占比逐年增加。'''
def stats_text_en(text):
#    text=input('请输入英文:\n')
    count=10
    import collections
    if type(text) is str:
        x='*-,.!' #列出要替换的标点符号
#       words_dict={} #空字典
        for c in x: #按每个标点在X里面循环
            text=(text.replace(c,'')) #重置的text的值
        words=text.lower().split() #将text小写字母化后切片给words赋值
        r=collections.Counter(words).most_common(count)
#       z=b.most_common(5)
#       b=set(words) #将words去掉重复项赋值给B
#       for word in b: #在B里的每个单词循环
#           d=words.count(word) #计算每个单词在words里出现的次数，赋值给D
#           words_dict[word]=d #每个单词及出现的次数以字典的方式存储在words_dict
#       e=sorted(words_dict.items(),key=lambda t:t[1],reverse=True) #将字典里的项目按值的大小降序排列
        print(r) #打印E
    else: 
        raise ValueError('文本类型不是英文')
        print(ValueError.__context__)
    return
stats_text_en(text) 
def stats_text_cn  (text1): #定义函数stats_text_cn    
#    text1=input('请输入文字:\n')
    count=10
    import collections
    if type(text1) is str:
       import re               #导入模块
       i=r"[\u4e00-\u9fa5]"    #unicode代码库
       j= re.compile(i)        #将创建的模式对像赋值给J
       k= re.findall(j,text1)  #将与模式与文本匹配得到的unicode代码赋值给K
       q=collections.Counter(k).most_common(count)
#       dict={}                 #建空字典
#       for l in k:             #在K内每个字循环
#           m=k.count(l)        #计算每个字K里出现的次数赋值给M
#           dict[l]=m           #将每一项存入字典
#       q=sorted(dict.items(),key=lambda y:y[1],reverse=True) #字典项按出现次数降序
       print(q)                #打印排序后的结果
    else: 
        raise ValueError('文本类型不是字符串')
        print(ValueError.__context__)
    return                    #返回
stats_text_cn(text1) 
   
#def stats_text_en1 (text):
#    a = counter()
#    if type(text) is str:
#       x='*-,.!' #列出要替换的标点符号
#       for c in x: #按每个标点在X里面循环
#           text=text.replace(c,'')#重置的text的值
#           words=text.lower().split() #将text小写字母化后切片给words赋值
#    a=collections.Counter(words).most_common(10)
#    print(a)
#    return
#stats_text_en1(text)
def tang_count ():   
    count=100
    import collections
    import json
    import re
    with open('/Users/mayjiao/Documents/GitHub/selfteaching-python-camp/exercises/1901100169/D9/mymodule/tang300.json','r',encoding='utf-8') as f:
        k=f.read()
        j= re.compile(r"[\u4e00-\u9fa5]")      
        m= re.findall(j,k)  
        q=collections.Counter(m).most_common(count)
        print(q)
    return
tang_count()


 
    