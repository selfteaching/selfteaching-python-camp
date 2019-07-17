
#统计参数中每个英文单词出现的次数，按词频降序排列数组
from collections import Counter

def stats_text_en(text):
    if  not isinstance(text,str):
        raise TypeError('输入的不是文本格式')
    text = text.replace("\n"," ").replace(","," ").replace("."," ").replace("*"," ").replace("--"," ")
    '''d = {}
    for x in text.split():

        if x not in d:#and u'\u0061' <= x <= u'\u007a'

            d[x] =1
        else:
            d[x]=d[x]+1

    print (sorted(d.items(), key=lambda item: item[1],reverse=True)) '''
    count = 8
    print(Counter(text.split()).most_common(count))#day9 作业


#统计参数中每个汉字单词出现的次数，按字频降序排列数组

def stats_text_cn(text):
    if  not isinstance(text,str):
        raise TypeError('输入的不是文本格式')
    d = {}
    for x in text:
        if u'\u4e00' <= x <= u'\u9fff' :#u'\u0061' <= x <= u'\u007a'
            d[x] = text.count(x)
   # print(sorted(d.items(), key=lambda item: item[1], reverse=True))  #按出现数字从大到小排列
    '''for x in text:
        if u'\u4e00' <= x <= u'\u9fff' :#u'\u0061' <= x <= u'\u007a'''
            
    counter = 8   
    print(Counter(d).most_common(counter))#day9 作业
#分别调用stats_text_en , stats_text_cn 合并输出词频统计结果
def stats_text(text):
    
        stats_text_cn(text)
        stats_text_en(text)


