# encoding=utf 
# 调用jieba
import jieba #day10
#调用counter
import collections
import re

# 函数1：统计输入文本中英文单词的词频：
def stats_text_en(text,count):
    if not isinstance(text,str):
        raise ValueError('输入的不是文本格式，请重新输入：') # 第8天作业要求，添加参数类型检查
    text = text.replace('.', '').replace('!', '').replace('--', '').replace('*', '').replace(',', '').replace('(', '').replace(')', '').replace(';', '').replace(':', '').replace('\'', '').replace('?', '').replace('_', '').replace('-', '').replace('/', '') .replace('[', '') .replace(']', '') .replace('\\', '') .replace('\"', '').replace('{', '').replace('}', '').replace('\t', '').replace('\n', '').replace('\r\n', '')    
        
    # 以上替换去除各种标点符号
    list_text = text.split() # 将字符串转换为列表
    import collections
    dic = collections.Counter(list_text).most_common(count)
    return dic



# 函数2：统计输入文本中中文字的词频：
def stats_text_cn(text,count):  
    if not isinstance(text,str):
        raise ValueError('输入的不是文本格式，请重新输入：') # 第8天作业要求，添加参数类型检查
    
    text1 = []
    for i in text:  # 这个循环有效，说明一串汉字也是一个字符串，每个汉字就是其中的一个元素，可以用for in 来遍历，其中i代表了每个汉字的unicode编码
        if u'\u4e00' > i > u'\u9fff':     # 挑选出非中文字
            text=text.split(i,"") # 将非中文字符替换
    seg_list = jieba.cut(text,cut_all =False) 
    
    for j in seg_list:
             if len(j) >= 2 : #只统计长度大于等于2的词
              text1.append(j)
    text1 = collections.Counter(text1).most_common(count)  #按出现次数从大到小排列
    return text1


# 函数3：统计中英文混合词频：
def stats_text(text,count) :
    '''合并中英文词频'''
    '''参数类型检查，如果输入参数不为字符串抛出ValueError'''
    if  not  isinstance(text, str) :
        return(stats_text_en(text,count) + stats_text_cn(text,count))
    else:
        raise ValueError("输入的不是字符串")