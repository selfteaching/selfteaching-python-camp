
def stats_text_en(text):
    textlist1 = text.split() #形成单词列表，通过 string 的 split() 将字符串切成数组
    textlist2 = []             #表示定义一个列表，列表推导用方括号（“[]”）括起来
    for i in textlist1:              #对textlist1中的每个i都进行检测
        if i.isalpha():               #如果i是字母，则添加i到原来列表textlist2的最后。
           textlist2.append(i)      #去除非单词
    dict1 = {}                         #标准的映射类型字典。字典的键几乎是任意值
    dict1 = dict1.fromkeys(textlist2)  #对dict1改变成键值来自于textlist2
    word_1 = list(dict1.keys())        #赋值world_1是表dict1的键值
    for i in word_1:                    #对于每个在world_1里的i都进行遍历
        dict1[i] = textlist2.count(i)   #统计单词出现的次数 ，dict1里面的i，等于在textlist2中出现的次数
    dict2 = {}                           #让dict2等于{}
    dict2 = sorted(dict1.items(),key=lambda d:d[1],reverse=True) 
     #sorted(iterable, *, key=None, reverse=False)从iterable中的项返回一个新的排序列表。
     #reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
    dict2 = dict(dict2)                  
    #转化为字典     Create a new dictionary. The dict object is the dictionary class         
    print(dict2)
    return;

text = '''                        

Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.
好好学习天天向上，学习学习再学习,pony6666
'''
print()

stats_text_en(text)            #这个自定义的函数，可以极大地方便统计任何一篇英语文章中出现单词的频率



   
          

def stats_text_cn(text): 
    import re
     #stats 是统计。cn是Chinese。
    # remove chinese symbol and "\n" and " " and, don't forget english and number charactor... 
    i = re.compile("[，；。—~ ？!‘’“”,.'*-_\nA-Za-z0-9]")
    text_rm_symbol = i.sub("", text)  #？这里的式子不知都什么意思，""这个不知道有什么意义
 
    # split
    text_to_list = []              #定义一个列表
    for x in text_rm_symbol:        #字符串弄成列表的形式
        text_to_list.append(x) 
    while "" in text_to_list:       #去掉""这个东西
        text_to_list.remove("")      #最后剩下只有汉字的列表
    # create dictionary              #创作一个字典
    sort_list = [(x, text_to_list.count(x)) for x in set(text_to_list)]#列表是可变类型，可以用sort对列表进行排序
                                                                       #？不知道set有什么作用
    sort_dict = dict(sort_list)                                        #创造一个字典
    # output a dictionary sort by frequency 
    return (sorted(sort_dict.items(), key=lambda x: x[1], reverse=True)) #?lambda是什么意思
     #sorted(iterable, *, key=None, reverse=False)从iterable中的项返回一个新的排序列表。
     #reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
print(stats_text_cn(text))      #字符串的形式

print(dict(stats_text_cn(text)))#字典的形式


###############另外一个稍微简单的英语单词统计，中文汉字统计的程序####################

text = '''

 学习学习再学习

 Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.
'''
dict1 = {}
dict2 = {} 
dict3 = {} 
dict4 = {}
 
def stats_text_en(text):   #创建一个名为stats_text_en的函数 
    import re 
    text = re.sub("[^A-Za-z]", " ", text.strip())   #只保留英文
    list1 = re.split(r"\W+",text)   #将字符串text转换为列表list1,只保留单词为list1中的元素 
    while '' in list1:   #删除list1中为空的列表元素 
        list1.remove('') 
    for i in list1:    
        dict1.setdefault(i,list1.count(i))  #将列表中的单词及单词的出现次数，分别赋值给dict1的键和值 
    tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)   #将dict1按照value值从大到小排列，并将结果赋给元组tup1
    for tup1 in tup1:   
 
            dict2[tup1[0]] = dict1[tup1[0]]  
    return dict2
print(stats_text_en(text))
 


 
#封装一个统计中文字频的函数

cndic={}                        #创建一个空的字典
 
def stats_text_cn(checkstr):    #定义检索中文函数
    for i in checkstr:          # 如果字典里有该单词则加1，否则添加入字典
        if u'\u4e00' <= i <= u'\u9fff':   #判断一个unicode是否是汉字 
            cndic[i] = checkstr.count(i)   
    return cndic
 
#一个中英混杂的文本 
text = '''                        
好好学习天天向上，学习学习再学习,pony6666
'''
stats_text_cn(text)             #调用检索中文频次的函
cndic=sorted(cndic.items(),key=lambda item:item[1],reverse = True)      #检索完毕后对字典进行按值从大到小排序
print(cndic)


############    另一个更简单的    统计英文词频和汉语字频的程序

#英文词频统计函数

import  re   
#英文单词统计函数
def  stats_text_en(text):
    a=re.sub(r'[^A-Za-z]',' ',text)    #只取英文单词
    str=a.split()                      #单词划分
    wordcount={}
    for i in str:             
        wordcount[i]=str.count(i)     #词频统计词典设置
    wordcount=sorted(wordcount.items(),key=lambda x:x[1],reverse=True)    #词频统计，按词频降序排列
    print(wordcount) #输出英文单词频数统计结果
    return 
print(stats_text_en(text))

#中文频数统计函数
def  stats_text_cn(text):
    p =  re.compile(r'[\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5
    res = re.findall(p, text)   #取中文
    wordcount={}                 #词频统计字典初始化
    for i in res:             
        wordcount[i]=res.count(i)     #词频统计词典设置
    wordcount=sorted(wordcount.items(),key=lambda x:x[1],reverse=True)    #词频统计，按词频降序排列
    print(wordcount)  #输出每个中文汉字频数统计结果
    return
print(stats_text_cn(text))