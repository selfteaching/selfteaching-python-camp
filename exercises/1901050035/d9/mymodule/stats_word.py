#Selfteaching day9 homework , updating by Counter function !

#1.En 
def stats_text_en(text,count): # 统计英文单词出现的次数
    """Return a list containing English word's counts by count value."""# 使用文档字符串说明
    if not isinstance(text,str):     ##如果不是字符串，抛出异常
        raise ValueError ("input text is not string type") 
    
    from collections import Counter
    import re
    
    count=int(count) #限制输出字符个数
    t1=re.findall(r'[a-z]\w+', text.lower())
    d1=Counter() # Counter 
    for word in t1:
            d1[word] += 1  #将单词计数统计    
      #print(d1)
    d2 = Counter(d1).most_common(count)   
    #d2 = sorted(d1.items(),key = lambda x:x[1],reverse = True)
    #print(d2)
    return d2 #按count值有序返回统计结果

#2.Cn
 
def stats_text_cn(text,count):  # 统计每个中文字出现的次数
    """Return a list containing chinese word's counts by count value """  # 使用文档字符串说明
    if not isinstance(text,str):     #如果不是字符串，抛出异常
        raise ValueError ("input text is not string type") 
    from collections import Counter
    import re
    
    count=int(count)  #限制输出字符个数
    t1=re.findall(u"([\u4e00-\u9fff])", text)
    d1=Counter() # 调用Counter 
    for word in t1:
            d1[word] += 1  #将单词计数统计
    #print(d1)  
    d2 = Counter(d1).most_common(count)
    #d3 = sorted(d1.items(), key=lambda item: item[1], reverse=True)  #将d1按照value值从大到小降序排列
    return d2 #按count值有序返回统计结果

#3.En+Cn
def stats_text(text,count): 
    """Return a list containing english and chinese word's counts by count value """ # 使用文档字符串说明
    if not isinstance(text,str):     ##如果不是字符串，抛出异常
        raise ValueError ("input text is not string type") 
    d3=[]
    d3=stats_text_cn(text,count)+stats_text_en(text,count) # 分别调用英文和中文统计结果
    
    #print(d3)
    return d3 ##按count值有序返回统计结果
 