from collections import Counter
import re
re_en = re.compile(r'[\u0061-\u007a,\u0020]') #用正常表达式获取所有的英文和空格，为了能达到单词需要保留空格
re_cn = re.compile(r'[\u4E00-\u9FA5]') #用正常表达式获取所有的汉字


def stats_text_cn (text:'输入的文本',count) -> list:
    if not isinstance(text,str):
        raise ValueError('stats_text_cn函数需要的参数是字符串')
    cn_text_list=re_cn.findall(text) 
    count_cn=Counter(cn_text_list).most_common(count)#用counter统计列表的元素，用count限制个数
    return count_cn


def stats_text_en (text:'输入的文本',count) -> list:
    if not isinstance(text,str):
        raise ValueError('stats_text_en函数需要的参数是字符串')
    en_text=''.join(re_en.findall(text))  #截取英文和空格，拼接成带单词的字符串
    en_text_list=en_text.split() #截取出单词，存在列表里
    count_en=Counter(en_text_list).most_common(count)#用counter统计列表的元素，用count限制个数
    return count_en 
  
    
