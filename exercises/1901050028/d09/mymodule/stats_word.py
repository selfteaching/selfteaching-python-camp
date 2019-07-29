import collections
import re

def stats_text_en(text,count): 
    '''该函数返回一个英文单词词频统计，样式为（word,count）'''
    t = text.replace(',',' ').replace('.',' ').replace('-',' ').replace('"',' ').replace('!',' ').replace('?',' ') #替换标点为空格
    if type(text)!=str:
        raise ValueError('输入参数非字符串')
    list = ''   #存储英文单词的字符串
    
    for s in t:  # 只保留英文单词
        if s.isascii():
            list += s

    t1= list.split()
    return collections.Counter(t1).most_common(count)

        
def stats_text_cn(text,count):
    if type(text)!=str:
        raise ValueError('输入参数非字符串')
    dict={}
    for i in text:
        if u'\u4e00' <= i <= u'\u9fa5': #提取中文汉字，\u是unincode编码，u4e00是十六进制表达值
            dict[i]=text.count(i) 
    return collections.Counter(dict).most_common(count)

    
def stats_text(text,count):
    if type(text)!=str:
        raise ValueError('输入参数非字符串')
    else:
        return stats_text_cn(text,count)+stats_text_en(text,count)
    
