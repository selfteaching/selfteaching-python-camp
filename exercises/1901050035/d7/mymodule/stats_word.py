#Selfteaching day7 homework ,creat a module !

def stats_text_en(text):# 统计英文单词出现的次数
    """Return a list containing English word's counts in decrease."""# 使用文档字符串说明
    import re
    t1=text.lower() #将text lower
    t2=[]
    pttn = r'[a-z]\w+'
    t2=re.findall(pttn, t1)
    d1={} #define dict
    for i in t2:
        d1.setdefault(i,t2.count(i))  #将单词及单词的出现次数，分别赋值给d1的KEY和vaule
      #print(d1)
    d2 = sorted(d1.items(),key = lambda items:items[1],reverse = True)
     #print(d2)
    return d2 #返回统计结果，出现次数从大到小降序输出

 
def stats_text_cn(text):  # 统计每个中文字出现的次数
    """Return a list containing chinese word's counts in in decrease """  # 使用文档字符串说明
    t1=text
    d1={}
    for i in t1:
        if u'\u4e00' <= i <= u'\u9fff':  #调用中文正则表达式
            d1.setdefault(i,t1.count(i))
    #print(d1)  
    d3 = sorted(d1.items(), key=lambda item: item[1], reverse=True)  #将d1按照value值从大到小降序排列
    return d3 #返回统计结果，次数从大到小降序输出
            
def stats_text(text): 
    """Return a list containing english and chinese word's counts in in decrease """ # 使用文档字符串说明 
    d3=[]
    d3=stats_text_cn(text)+stats_text_en(text) # 分别调用英文和中文统计结果 
    #print(d3)
    return d3 #返回统计结果
    
    
    
    
    