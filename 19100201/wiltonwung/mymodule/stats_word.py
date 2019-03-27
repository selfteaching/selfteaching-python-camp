

dict1 = {} #设立数据容器
dict2 = {}
dict3 = {}
dict4 = {}

def stats_text_en(text):  #设定函数 
    import re #引入系统函数
    text = re.sub("[^A-Za-z]", " ", text.strip())  #只留英语单词
    list1 = re.split(r"\W+",text)   #把单词存入一个list里
    
    while '' in list1:   
        list1.remove('')  #删除空格
    
    for i in list1:   
        
        dict1.setdefault(i,list1.count(i))  #把单词极其频次统计到一个字典里
   
    tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)   #按照字频排序 

    for tup1 in tup1:   
            dict2[tup1[0]] = dict1[tup1[0]]  
    return dict2#组装到新字典中


    print(stats_text_en(text))#打印出英文词频


def histogram(s, old_d):#设置一个更新数量的函数
    d = old_d
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def stats_text_cn(text): #只针对汉字的函数
    import re
    text = re.sub("[A-Za-z0-9]", "", text) #遴选出汉字

    list1 = re.split(r"\W+",text)   #分割汉字

    while '' in list1:   
        list1.remove('') #去除空格

    dict3 = dict()        #use dict function
    
    for i in range(len(list1)):
        dict3 = histogram(list1[i], dict3)

    
    tup1 = sorted(dict3.items(),key = lambda items:items[1],reverse = True)  

    for tup1 in tup1:   
            dict4[tup1[0]] = dict3[tup1[0]]  
    return dict4

#print(stats_text_cn(text))#统计汉字


def stats_text(text):
    return dict(stats_text_en(text),**stats_text_cn(text))
    

