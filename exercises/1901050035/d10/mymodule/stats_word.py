#Selfteaching day10 homework , updating by jieba one of 3rd libs!

#1.Cn
 
def stats_text_cn(text,count):  # 统计每个中文字出现的次数
    """Return a list containing chinese word's counts by count value """  # 使用文档字符串说明
    if not isinstance(text,str):     #如果不是字符串，抛出异常
        raise ValueError ("input text is not string type") 
    
    from collections import Counter
    import re
    import jieba
    
    count = int(count)  #限制输出字符个数
    text = re.sub(r'[a-zA-Z0-9_]','', text) #删除非中文字符
    
    l1=jieba.cut(text, cut_all=False)   #调用jieba精确分词
    l2=list(x for x in l1 if len(x)>=2)  #仅统计词长大约等于2的
    
    d1=Counter() # 调用Counter 函数
    for word in l2:
        d1[word] += 1  #将单词计数统计
    #print(d1)  
    d2 = Counter(d1).most_common(count)
    #d3 = sorted(d1.items(), key=lambda item: item[1], reverse=True)  #将d1按照value值从大到小降序排列
    return d2  #按count值有序返回统计结果

#cn anoher way
def stats_text_cn_u(text,count):  # 统计每个中文字出现的次数
    """Return a list containing chinese word's counts by count value """  # 使用文档字符串说明
    if not isinstance(text,str):     #如果不是字符串，抛出异常
        raise ValueError ("input text is not string type") 

    from collections import Counter
    import re
    import jieba

    count = int(count)  #限制输出字符个数
    t1=re.findall(u"([\u4e00-\u9fff])", text)
    #text = re.sub(r'[a-zA-Z0-9_]','', text) #删除非中文字符
    t1 = ''.join(t1)              #合并中文字符
    l1=jieba.cut(t1, cut_all=False)   #调用jieba精确分词
    l2=list(x for x in l1 if len(x)>=2)  #仅统计词长大约等于2的

    d1=Counter() # 调用Counter 函数
    for word in l2:
        d1[word] += 1  #将单词计数统计
    #print(d1)  
    d2 = Counter(d1).most_common(count)
    #d3 = sorted(d1.items(), key=lambda item: item[1], reverse=True)  #将d1按照value值从大到小降序排列
    return d2  #按count值有序返回统计结果


 