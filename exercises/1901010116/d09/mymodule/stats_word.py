#封装统计英文单词词频的函数
from collections import Counter
import string
import re

def stats_text_en(text,count = None):
    if not isinstance(text,str): #检查参数类型是否为字符串
        raise ValueError('Oops! The first parameter was no valid string.')
    elif not isinstance(count,int) and count != None: #检擦输入的第二个参数是否为整数
        raise ValueError('Oops! The second parameter was no valid integer.')
    else:
        text = re.findall(r'\w+',text.lower(),re.A) #筛选英文单词，剔除其他文字

        #统计单词出现次数  
        f = Counter(text).most_common(count)
        return f

#封装统计中文汉字字频的函数
def stats_text_cn(text,count = None):
    if not isinstance(text,str): #检查参数类型是否为字符串
        raise ValueError('Oops! The first parameter was no valid string.')
    elif not isinstance(count,int) and count != None: #检擦输入的第二个参数是否为整数
        raise ValueError('Oops! The second parameter was no valid integer.')
    else:
        text = re.findall(r'[\u4E00-\u9FA5]',text) #只留下汉字，剔除其他字符

        #统计汉字出现次数
        f = Counter(text).most_common(count)
        return f

#分别调⽤stats_text_en , stats_text_cn ，输出合并词频统计结果
def stats_text(text,count = None):
    """
    统计英文单词及中文汉字出现的频次
    
    参数为字符串
    返回一个数列
    """
    if not isinstance(text,str): #检查参数类型是否为字符串
        raise ValueError('Oops! The first parameter was no valid string.')
    elif not isinstance(count,int) and count != None: #检擦输入的第二个参数是否为整数
        raise ValueError('Oops! The second parameter was no valid integer.')     
    else:
        return stats_text_en(text,count) + stats_text_cn(text,count)
