import re
import collections
import jieba
#统计参数中每个英文单词出现的次数，按词频降序排列数组
def stats_text_en(text,count):
    if not isinstance(text,str):#判断参数类型
        raise ValueError("非字符串参数")#抛出异常类型'''

    text = re.sub("[^A-Za-z]+", " ", text)
    d = {}
    for x in text.split():
        if x not in d:
            d[x] =1
        else:
            d[x]+=1
    #return sorted(d.items(), key=lambda x: x[1],reverse=True)
    return collections.Counter(d).most_common(count)


#统计参数中每个汉字出现的次数，按字频降序排列数组
def stats_text_cn(text,count):
    '''统计参数中每个汉字出现的次数，按字频降序排列数组'''
    if not isinstance(text,str):#判断参数类型
        raise ValueError("非字符串参数")#抛出异常类型'''
    text=re.sub("[^\u4e00-\u9fa5]+","",text)
    text=jieba.cut(text,cut_all=False)
    d = []
    for x in text:
        if len(x)>=2:
            d.append(x)
    #return sorted(d.items(), key=lambda x: x[1], reverse=True) #按出现数字从大到小排列
    
    return collections.Counter(d).most_common(count)

# 函数3：统计中英文混合词频：
def stats_text(text,count):
    '''函数说明：
    本函数的功能是统计输入文本的汉字及英语单词词频，并以降序排列输出。'''
    if not isinstance(text,str):#判断参数类型
        raise ValueError("非字符串参数")#抛出异常类型'''
    d1 = stats_text_en(text,count)
    d2 = stats_text_cn(text,count)
    d3 = {}
    d3.update(d2)
    d3.update(d1)
    return collections.Counter(d3).most_common(count)
    #return (stats_text_en(text,count) + stats_text_cn(text,count))
#print(stats_text(text))

#print(stats_text.__doc__)


